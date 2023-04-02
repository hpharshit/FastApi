from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel


app = FastAPI()

# @app is path operation decorator, 'get' is operation


@app.get("/")  # sending response to '/' path from http://127.0.0.1:8000
def index():  # path operation function called on  '@app.get("/") '
    return {
        'data': "Blog List"
    }


@app.get("/blog/unpublished")
def unpublished():
    return {
        'data': "unpublished"
    }


@app.get("/blog")
# expecting query-param  http://127.0.0.1:8000/blog?limit=10&published=true
# setting datatypes and giving default values
def blogwithquery(limit: int = 10, published: bool = True, sort: Optional[str] = None):
    if (published == True):
        return {
            'data': f'{limit} published blogs being displayed'
        }

    else:
        return {
            'data': f'{limit} blogs being displayed'

        }


@app.get("/blog/{id}")  # path-param
# this 'id' parameter must match param name 'id' in @app.get("/blog/{id}")
def blogwithid(id: int):  # accepting param and defining datatype of param (coverts string 'id' to int value of 'id')
    return {
        'data': id
    }


@app.get("/blog/{id}/comments")
def comments(id):  # path operation function called on  '@app.get("/about") '
    return {
        'data': {'1', '2', id}
    }


# Creating Schema
# class Blog(BaseModel):
#     title: str
#     body: str
#     published: Optional[bool]


# @app.post("/blog")
# def create_blog(request: Blog):
#     return {"data": f"Blog created with Title: {request.title}, Body: {request.body}, Published: {request.published}"}
#  uvicorn main:app --reload

# to change port : run using python main.py
# if(__name__=="__main__"):
#     uvicorn.run(app,host="127.0.0.1",port=9000);
