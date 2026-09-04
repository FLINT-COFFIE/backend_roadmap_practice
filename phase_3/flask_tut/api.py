from flask import Flask, request, jsonify

app = Flask(__name__)

books = [
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
