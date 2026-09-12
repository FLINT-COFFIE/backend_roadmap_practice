# Imports

from random import randrange

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

# Instance of fastapi
app = FastAPI()


# making a post base model
class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: int | None = None


# finding one post
def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p


# finding post index
def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p["id"] == id:
            return i


# error post
def raise_404(id):
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"post with id {id} was not found",
    )


# saving posts in memory
my_posts = [
    {
        "id": 1,
        "title": "Why Butter Chicken is Worth Every Calorie",
        "content": "A deep dive into the rich, velvety tomato and butter sauce that makes this dish an absolute masterpiece. Paired with freshly baked garlic naan, it is comfort food at its finest.",
    },
    {
        "id": 2,
        "title": "The Masterclass in Sci-Fi: Interstellar",
        "content": "Christopher Nolan's space epic blends hard theoretical physics with an emotional core about family. Hans Zimmer's pipe organ score alone elevates it to legendary status.",
    },
    {
        "id": 3,
        "title": "The Art of the Perfect Espresso Shot",
        "content": "Variables like grind size, water temperature, and extraction time can make or break your morning brew. Dialing in your grinder is a journey of endless patience and reward.",
    },
    {
        "id": 4,
        "title": "Why Studio Ghibli's Spirited Away Never Ages",
        "content": "Hayao Miyazaki's hand-drawn animation creates a living, breathing spirit world that feels both terrifying and deeply welcoming. It remains a timeless coming-of-age allegory.",
    },
]


# path operations
@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/posts")
def get_posts():
    return {"data": my_posts}


@app.get("/posts/{id}")
def get_one_post(id: int):
    post = find_post(id)
    if not post:
        raise_404(id)
    return {"data": post}


@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
    post_dict = post.model_dump()
    post_dict["id"] = randrange(0, 1000000000000)
    my_posts.append(post_dict)
    return {"data": post_dict}


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    index = find_index_post(id)
    if index is None:
        raise_404(id)
    my_posts.pop(index)
