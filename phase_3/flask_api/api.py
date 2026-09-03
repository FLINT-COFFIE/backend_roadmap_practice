# importing Flask
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# making an instance of Flask
app = Flask(__name__)

# location and name of db
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)


# user data
class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)

    # user info
    def __repr__(self):
        return f"User(name = {self.name}, email = {self.email}"


# making routes
@app.route("/")
def home():
    return "<h1>Flask Rest Api</h1>"


if __name__ == "__main__":
    app.run(debug=True)
