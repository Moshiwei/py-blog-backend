from elasticsearch import Elasticsearch, helpers
from elasticsearch.exceptions import NotFoundError
from resources.blog import get_all_blogs

class ElasticsearchClient:
    def __init__(self, hosts=None, timeout=30):
        """
        初始化 Elasticsearch 客户端
        :param hosts: Elasticsearch 节点地址列表，默认为 ['localhost:9200']
        :param timeout: 请求超时时间，默认为 30 秒
        """
        self.hosts = hosts or ['http://localhost:9200']
        self.client = Elasticsearch(hosts=self.hosts, request_timeout=timeout, 
                                    api_key="QkZtM0JKVUJnWWQ0dUdRdV9LTWw6TmtuWjUzQ0JUcU9RZUNtc2VOVTNMUQ==")
        print("Connect OK")

    def create_index(self, index_name, mappings=None, settings=None):
        """
        创建索引
        :param index_name: 索引名称
        :param mappings: 索引的映射（字段类型定义）
        :param settings: 索引的设置（分片、副本等）
        :return: 创建结果
        """
        body = {}
        if mappings:
            body["mappings"] = mappings
        if settings:
            body["settings"] = settings

        return self.client.indices.create(index=index_name, body=body)  # ignore=400 表示如果索引已存在则忽略

    def delete_index(self, index_name):
        """
        删除索引
        :param index_name: 索引名称
        :return: 删除结果
        """
        return self.client.indices.delete(index=index_name, ignore=[400, 404])  # ignore=404 表示如果索引不存在则忽略

    def index_document(self, index_name, document, doc_id=None):
        """
        插入或更新文档
        :param index_name: 索引名称
        :param document: 文档内容（字典格式）
        :param doc_id: 文档 ID（可选，如果不提供则自动生成）
        :return: 插入结果
        """
        return self.client.index(index=index_name, id=doc_id, document=document)

    def get_document(self, index_name, doc_id):
        """
        获取文档
        :param index_name: 索引名称
        :param doc_id: 文档 ID
        :return: 文档内容
        """
        try:
            return self.client.get(index=index_name, id=doc_id)
        except NotFoundError:
            return None

    def update_document(self, index_name, doc_id, updated_fields):
        """
        更新文档
        :param index_name: 索引名称
        :param doc_id: 文档 ID
        :param updated_fields: 需要更新的字段（字典格式）
        :return: 更新结果
        """
        return self.client.update(index=index_name, id=doc_id, doc=updated_fields)

    def delete_document(self, index_name, doc_id):
        """
        删除文档
        :param index_name: 索引名称
        :param doc_id: 文档 ID
        :return: 删除结果
        """
        return self.client.delete(index=index_name, id=doc_id, ignore=[404])  # ignore=404 表示如果文档不存在则忽略

    def search_documents(self, index_name, query):
        """
        查询文档
        :param index_name: 索引名称
        :param query: 查询条件（Elasticsearch Query DSL）
        :return: 查询结果
        """
        return self.client.search(index=index_name, body=query)

    def bulk_index(self, index_name, documents):
        """
        批量插入文档
        :param index_name: 索引名称
        :param documents: 文档列表（每个文档为字典格式）
        :return: 批量插入结果
        """
        actions = [
            {
                "_index": index_name,
                "_source": document
            }
            for document in documents
        ]
        return helpers.bulk(self.client, actions)

    def bulk_update(self, index_name, updates):
        """
        批量更新文档
        :param index_name: 索引名称
        :param updates: 更新列表（每个更新为字典格式，包含文档 ID 和更新内容）
        :return: 批量更新结果
        """
        actions = [
            {
                "_op_type": "update",
                "_index": index_name,
                "_id": update["doc_id"],
                "doc": update["updated_fields"]
            }
            for update in updates
        ]
        return helpers.bulk(self.client, actions)

    def bulk_delete(self, index_name, doc_ids):
        """
        批量删除文档
        :param index_name: 索引名称
        :param doc_ids: 文档 ID 列表
        :return: 批量删除结果
        """
        actions = [
            {
                "_op_type": "delete",
                "_index": index_name,
                "_id": doc_id
            }
            for doc_id in doc_ids
        ]
        return helpers.bulk(self.client, actions)

    def close(self):
        """
        关闭 Elasticsearch 客户端连接
        """
        self.client.close()
