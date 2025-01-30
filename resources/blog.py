from db import db
from models.blog import BlogPost

def add_blog():
    pass

def get_all_blogs():
    sql = "SELECT * FROM blogs"
    blogs = db.query(sql)
    # no need to add this line, because the content fetched from db is OK directly.
    # serialized_res = [BlogPost(**dict(blog)) for blog in blogs]
    return blogs
    

def get_blog():
    pass

def update_blog():
    pass

def delete_blog():
    pass