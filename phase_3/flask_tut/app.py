# Importing Flask
from flask import Flask

# basic flask app
app = Flask(__name__)


# creating a route
@app.route("/")
def home():
    return "Hello World"


# Running it programatically
if __name__ == "__main__":
    app.run()
