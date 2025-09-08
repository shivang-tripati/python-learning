from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel


app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    publish: bool = True
    rating: int | None = None

@app.get("/")
def root():
    return {"message": "hello world, It's Fast Api"}

@app.post("/createposts")
def create_post(new_post: Post = Body(...)):
    print(new_post.publish)
    return {"new_post": new_post}