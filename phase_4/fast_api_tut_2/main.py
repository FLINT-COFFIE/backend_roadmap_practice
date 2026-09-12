# Imports
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

# Instance of fastapi
app = FastAPI()


# making a post base model
class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


# path operations
@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/posts")
def get_posts():
    return {"data": "This is your posts"}


@app.post("/posts")
def create_posts(post: Post):
    print(post.title)
    return {"data": "new post"}
