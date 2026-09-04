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


# default route
@app.route("/")
def home():
    return "Welcome"


# create and read route for books
@app.route("/books", methods=["GET", "POST"])
# view function
def books():
    # reading the books
    if request.method == "GET":
        if len(books_list) > 0:
            # returning the books as a response
            return jsonify(books_list)
        else:
            "Nothing Found", 404  # error code

    # creating a new book
    if request.method == "POST":
        new_author = request.form["author"]
        new_lang = request.form["language"]
        new_title = request.form["title"]
        new_id = books_list[-1]["id"] + 1

        new_book = {
            "id": new_id,
            "author": new_author,
            "language": new_lang,
            "title": new_title,
        }

        books_list.append(new_book)
        return jsonify(books_list), 201  # success code


# reading single books
# adding update and delete
@app.route("/books/<int:id>", methods=["GET", "PUT", "DELETE"])
def single_book(id):
    # reading the books
    if request.method == "GET":
        for book in books_list:
            if book["id"] == id:
                # returning the books as a response
                return jsonify(book)

    # updating the table
    if request.method == "PUT":
        for book in books_list:
            if book["id"] == id:
                book["author"] = request.form["author"]
                book["language"] = request.form["language"]
                book["title"] = request.form["title"]

                # updating books list
                updated_book = {
                    "id": id,
                    "author": book["author"],
                    "language": book["language"],
                    "title": book["title"],
                }
                return jsonify(updated_book)

    # deleting books
    if request.method == "DELETE":
        for index, book in enumerate(books_list):
            if book["id"] == id:
                books_list.pop(index)
                return jsonify(books_list)


if __name__ == "__main__":
    app.run(debug=True)
