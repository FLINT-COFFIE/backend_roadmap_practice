# Imports

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import auth, posts, users, vote

# making the database
# models.Base.metadata.create_all(bind=engine)

# Instance of fastapi
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def hello_world():
    return {"message": "Hello World"}


# added so path operations in posts and users with router. work
app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(vote.router)
