# learning flask

# importing flask and making use of the templates
from flask import Flask, render_template

# making an instance of flask
app = Flask(__name__)

# sample blog post

posts = [
    {
        "author": "Flint Coffie",
        "title": "The advantages of being self taught",
        "post_no": "Blog post 1",
        "date_posted": "September 1, 2026",
    },
    {
        "author": "Priscilla Coffie",
        "title": "The disadvantages of being self taught",
        "post_no": "Blog post 2",
        "date_posted": "September 2, 2026",
    },
]


# these are routes on the pages
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title="About")


# if run directly changes will show and pages only need to be refreshed.
if __name__ == "__main__":
    app.run(debug=True)
