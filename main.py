from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
  return {"message": "Hello, World!"}

@app.get("/about")
def about():
  return {"message": "About this API"}

@app.get("/user/{id}")
def user(id: int):
  return {"user": {"id": id}}

