# Imports

from fastapi import FastAPI
from pydantic import BaseModel

# Instance of fastapi
app = FastAPI()


# making a post base model
class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: int | None = None


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
    return {"data": "This is your posts"}


@app.post("/posts")
def create_posts(post: Post):
    print(post.title)
    return {"data": "new post"}
