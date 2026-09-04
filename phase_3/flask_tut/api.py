from flask import Flask, jsonify, request

app = Flask(__name__)

books_list = [
    {
        "id": 1,
        "title": "Things Fall Apart",
        "author": "Chinua Achebe",
        "language": "English",
    },
    {
        "id": 2,
        "title": "One Hundred Years of Solitude",
        "author": "Gabriel García Márquez",
        "language": "Spanish",
    },
    {
        "id": 3,
        "title": "The Little Prince",
        "author": "Antoine de Saint-Exupéry",
        "language": "French",
    },
    {
        "id": 4,
        "title": "Kafka on the Shore",
        "author": "Haruki Murakami",
        "language": "Japanese",
    },
    {
        "id": 5,
        "title": "Crime and Punishment",
        "author": "Fyodor Dostoevsky",
        "language": "Russian",
    },
]


# create and read route for books
@app.route("/books", methods=["GET", "POST"])
# view function
def books():
    if request.method == "GET":
        if len(books_list) > 0:
            # returning the books as a response
            return jsonify(books_list)
        else:
            "Nothing Found", 404  # error code
