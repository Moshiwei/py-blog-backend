from fastapi import FastAPI, HTTPException
from models.blog import BlogPost
from typing import List
from init import init_db
from resources.blog import get_all_blogs

# def init_app():
#     init_db()
#     print("Database initialized")

app = FastAPI()

# @app.post("/posts/", response_model=BlogPost)
# def create_post(post: BlogPost):
#     blog_posts.append(post)
#     return post
@app.get("/")
def index():
    return "Hello, FastAPI"

@app.get("/posts/", response_model=List[BlogPost])
def get_posts():
    blogs = get_all_blogs()
    return blogs

@app.get("/posts/{post_id}", response_model=BlogPost)
def get_post(post_id: int):
    for post in blog_posts:
        if post.id == post_id:
            return post
    raise HTTPException(status_code=404, detail="Post not found")

# @app.put("/posts/{post_id}", response_model=BlogPost)
# def update_post(post_id: int, updated_post: BlogPost):
#     for index, post in enumerate(blog_posts):
#         if post.id == post_id:
#             blog_posts[index] = updated_post
#             return updated_post
#     raise HTTPException(status_code=404, detail="Post not found")

# @app.delete("/posts/{post_id}", response_model=BlogPost)
# def delete_post(post_id: int):
#     for index, post in enumerate(blog_posts):
#         if post.id == post_id:
#             deleted_post = blog_posts.pop(index)
#             return deleted_post
#     raise HTTPException(status_code=404, detail="Post not found")