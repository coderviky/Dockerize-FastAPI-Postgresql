from typing import List, Optional
from pydantic import BaseModel


# class ItemBase(BaseModel):


class Item(BaseModel):
    title: str
    body: str
    comment: Optional[str] = None

    class Config():
        orm_mode = True


class UpdateItem(BaseModel):
    title: Optional[str] = None
    body: Optional[str] = None
    comment: Optional[str] = None

    # class Config():
    #     orm_mode = True


class ShowUser(BaseModel):
    name: str
    email: str

    class Config():
        orm_mode = True


class ShowItem(BaseModel):
    id: int
    title: str
    body: str
    creator: ShowUser

    class Config():
        orm_mode = True
