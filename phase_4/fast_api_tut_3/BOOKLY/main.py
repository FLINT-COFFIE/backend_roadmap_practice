from http.client import HTTPException

from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def read_root():
    return {"message": "Hello World"}


@app.get("/greet")
async def greet_name(name: str | None = "User", age: int = 0) -> dict:
    return {"message": f"Hello {name}", "age": age}


# class BookCreateModel(BaseModel):
#     title: str
#     author: str


# sample

# @app.post("/create_book")
# async def create_book(book_data: BookCreateModel):
#     return {"title": book_data.title, "author": book_data.author}


# getting headers
# @app.get("/get_headers")
# async def get_headers(accept: str = Header(None)):
#     request_headers = {}
#     request_headers["Accept"] = accept
#     return request_headers


books = [
    {
        "id": 1,
        "title": "Think Python",
        "author": "Allen B. Downey",
        "publisher": "O'Reilly Media",
        "published_date": "2021-01-01",
        "page_count": 1234,
        "language": "English",
    },
    {
        "id": 2,
        "title": "Fluent Python",
        "author": "Luciano Ramalho",
        "publisher": "O'Reilly Media",
        "published_date": "2022-05-15",
        "page_count": 1014,
        "language": "English",
    },
    {
        "id": 3,
        "title": "The WebSocket Protocol",
        "author": "Alex Diaconu",
        "publisher": "Xinyu Wang",
        "published_date": "2021-01-10",
        "page_count": 3677,
        "language": "English",
    },
    {
        "id": 4,
        "title": "FastAPI Web Development",
        "author": "Sanjeev Thiyagarajan",
        "publisher": "Packt Publishing",
        "published_date": "2023-08-20",
        "page_count": 450,
        "language": "English",
    },
    {
        "id": 5,
        "title": "Python High Performance",
        "author": "Gabriele Lanaro",
        "publisher": "Packt Publishing",
        "published_date": "2020-11-30",
        "page_count": 320,
        "language": "English",
    },
]


class Book(BaseModel):
    id: int
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str


class BookUpdateModel(BaseModel):
    title: str
    author: str
    publisher: str
    page_count: int
    language: str


# read
@app.get("/books", response_model=list[Book])
async def get_all_books():
    return books


@app.get("/book/{book_id}")  # , response_model=list[Book])
async def get_a_books(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")


# create
@app.post("/books")
async def create_a_book(book_data: Book, status_code=status.HTTP_201_CREATED) -> dict:
    new_book = book_data.model_dump()
    books.append(new_book)
    return new_book


# update
@app.patch("/book/{book_id}")
async def update_book(book_id: int, book_update_data: BookUpdateModel) -> dict:
    for book in books:
        if book["id"] == book_id:
            book["title"] = book_update_data.title
            book["author"] = book_update_data.author
            book["publisher"] = book_update_data.publisher
            book["page_count"] = book_update_data.page_count
            book["language"] = book_update_data.language
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")


# delete
@app.delete("/book/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_a_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
