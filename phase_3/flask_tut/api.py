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


if __name__ == "__main__":
    app.run(debug=True)
