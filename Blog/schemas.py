from typing import Optional, List
from pydantic import BaseModel
# pydantic model is for request and response to fastapi


# Creating Blog-Model
class Blog(BaseModel):
    title: str
    body: str
    class Config():
        orm_mode = True


# Creating user-Model
class User(BaseModel):
    name: str
    email: str
    password: str


class ShowUser(BaseModel):
    name: str
    email: str
    blogs: List[Blog]=[]

    class Config():
        orm_mode = True


class ShowBlog(BaseModel):
    title: str
    body: str
    creator: ShowUser

    class Config():
        orm_mode = True


class Login(BaseModel):
    username: str
    password: str

    class Config():
        orm_mode = True



class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None
