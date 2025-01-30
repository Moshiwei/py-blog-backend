from ..db import execute_sql
from ..models import BlogPost

def add_blog():
    pass

def get_all_blogs():
    sql = "SELECT * FROM blogs"
    blogs = execute_sql(sql)
    serialized_res = [BlogPost(**dict(blog)) for blog in blogs]
    return serialized_res
    

def get_blog():
    pass

def update_blog():
    pass

def delete_blog():
    pass