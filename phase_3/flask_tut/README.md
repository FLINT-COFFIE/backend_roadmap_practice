# Flask Book API

A lightweight REST API built with Flask to manage a book collection, featuring full CRUD operations and in-memory state management.

## Endpoints

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/` | Welcome check |
| `GET` | `/books` | Retrieve all books |
| `POST` | `/books` | Add a new book |
| `GET` | `/books/<id>` | Retrieve a single book by ID |
| `PUT` | `/books/<id>` | Update an existing book |
| `DELETE` | `/books/<id>` | Remove a book by ID |

## What I Learned
- Routing & Decorators: Mapping web paths to view functions using @app.route.

- HTTP Methods: Handling GET, POST, PUT, and DELETE requests within unified endpoints using request.method.

- Payload Parsing: Extracting and validating incoming JSON bodies via request.get_json().

- Status Codes & Responses: Returning structured JSON data paired with correct HTTP status codes (201 Created, 404 Not Found).

## Tech Stack
### Library: Flask