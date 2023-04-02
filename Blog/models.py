from .database import Base;
from sqlalchemy import Column, Integer, String,ForeignKey
# sqlalchemy  is for query processing
from sqlalchemy.orm import relationship


# Blog-model creation
class Blog(Base):
    __tablename__="blogs"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    user_id=Column(Integer,ForeignKey('users.id'))
    creator=relationship("User",back_populates="blogs")

# User-model creation
class User(Base):
    __tablename__="users"
    id = Column(Integer, primary_key=True, index=True)
    name= Column(String)
    email= Column(String)
    password= Column(String)
    blogs=relationship("Blog",back_populates="creator")
