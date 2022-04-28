from typing import List, Optional
from pydantic import BaseModel


class Item(BaseModel):
    title: str
    body: str

    class Config():
        orm_mode = True


class CreateUser(BaseModel):  #
    name: str
    email: str
    password: str


class ShowUser(BaseModel):
    name: str
    email: str
    items: List[Item] = []

    class Config():
        orm_mode = True


class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class User(BaseModel):  # current user
    id: int
    email: str
