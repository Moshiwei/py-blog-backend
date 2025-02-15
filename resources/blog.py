from db import db
from models.blog import BlogPost, CreatePost, UpdatePost

def add_blog(blog: CreatePost):
    # one big problem! forbid write sql by using format string which will cause sql syntaxError
    sql = """
        insert into blogs (title, content)
        values (%s, %s)
        returning *;
    """
    res = db.execute(sql, (blog.title, blog.content))

def get_all_blogs():
    sql = "SELECT * FROM blogs"
    blogs = db.query(sql)
    # no need to add this line, because the content fetched from db is OK directly.
    # serialized_res = [BlogPost(**dict(blog)) for blog in blogs]
    return blogs
    

def get_blog():
    pass


def update_blog(blog: UpdatePost):
    sql = """
        UPDATE blogs
        SET 
            title = '只更新标题',
            updated_at = CURRENT_TIMESTAMP
        WHERE id = %d;
    """
    db.execute(sql, blog.id)

def delete_blog():
    pass