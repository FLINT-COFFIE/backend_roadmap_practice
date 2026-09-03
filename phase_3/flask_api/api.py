# importing Flask
from flask import Flask

# making an instance of Flask
app = Flask(__name__)


# making routes
@app.route("/")
def home():
    return "<h1>Flask Rest Api</h1>"


if __name__ == "__main__":
    app.run(debug=True)
