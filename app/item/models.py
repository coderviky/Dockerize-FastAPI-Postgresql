from sqlalchemy import Column, Integer, String, ForeignKey
from core.database import Base
from sqlalchemy.orm import relationship
from auth.models import User


class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String,)
    comment = Column(String, nullable=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    creator = relationship("User", back_populates="items")


# class User(Base):
#     __tablename__ = 'users'

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String)
#     email = Column(String)
#     password = Column(String)

#     items = relationship('item', back_populates="creator")
