from pydantic import BaseModel
from datetime import datetime

class FullPost(BaseModel):
    id: int
    title: str
    content: str
    create_at: datetime
    update_at: datetime

class BlogPost(BaseModel):
    id: int
    title: str
    content: str

class CreatePost(BaseModel):
    title: str
    content: str

class UpdatePost(BlogPost):
    pass
    