# importing FastAPI
from fastapi import FastAPI

# creating an instance of FastAPI
app = FastAPI()


# making the api
@app.get("/")
def home():
    return {"name": "First Data"}
