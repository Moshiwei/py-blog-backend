from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models.blog import BlogPost, CreatePost
from typing import List
from init import init_db
from resources.blog import get_all_blogs, add_blog

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许所有域名访问，或者指定域名如 ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],  # 允许所有 HTTP 方法，或者指定方法如 ["GET", "POST"]
    allow_headers=["*"],  # 允许所有请求头
)

@app.get("/")
def index():
    return "Hello, FastAPI"

@app.get("/posts", response_model=List[BlogPost])
def get_posts():
    blogs = get_all_blogs()
    return blogs

@app.post("/posts")
def add_post(post: CreatePost):
    add_blog(post)

