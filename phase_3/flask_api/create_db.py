from api import app, db

# creating the database (placed in instance folder)
with app.app_context():
    db.create_all()
