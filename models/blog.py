from pydantic import BaseModel

class BlogPost(BaseModel):
    id: int
    title: str
    content: str

class CreatePost(BaseModel):
    title: str
    content: str
    