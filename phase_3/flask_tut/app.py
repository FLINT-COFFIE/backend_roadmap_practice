# Importing Flask
from flask import Flask

# basic flask app
app = Flask(__name__)


# creating a route
@app.route("/")
def home():
    return "Hello World"


# Dynamic Routing
@app.route("/<name>")
def print_name(name):
    return f"Greetings {name}"


# Running it programatically
# Added debug mode
if __name__ == "__main__":
    app.run(debug=True)
