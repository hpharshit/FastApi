from fastapi import FastAPI, Depends, status, Response, HTTPException
from . import schemas, models
from .hashing import Hash
from .database import engine
# from sqlalchemy.orm import Session
from typing import List
from .routers import blog,user,auth

app = FastAPI()

# when we find a new model then we create it on the database
models.Base.metadata.create_all(engine)

# including router file
app.include_router(auth.router);
app.include_router(blog.router);
app.include_router(user.router);

# # posting blogs
# @app.post("/blog", status_code=status.HTTP_201_CREATED, tags=['blogs'])
# def createBlog(request: schemas.Blog, db: Session = Depends(get_db)):
#     new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
#     db.add(new_blog)
#     db.commit()
#     db.refresh(new_blog)
#     return new_blog


# # getting all blogs from table
# @app.get("/blog", response_model=List[schemas.ShowBlog], tags=['blogs'])
# def getAllBlog(db: Session = Depends(get_db)):
#     blogs = db.query(models.Blog).all()
#     return blogs


# # getting blog with id from table
# @app.get("/blog/{id}", status_code=200, response_model=schemas.ShowBlog, tags=['blogs'])
# def getBlogWithId(id, db: Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id).first()
#     # returns sqlalchaemy model
#     if (blog == None):
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"Blog with the id={id} not found")
#     return blog

# # getting blog with id from table
# @app.get("/blog/{id}", status_code=200,response)
# def getBlogWithId(id, response: Response, db: Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id).first()
#     if (blog == None):
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"Blog with the id={id} not found")
#         # or
#         # response.status_code = status.HTTP_404_NOT_FOUND
#         # return {"details":f"Blog with the id={id} not found"}
#     return blog


# # deleting blog with id
# @app.delete("/blog/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=['blogs'])
# def deleteBlogWithId(id, db: Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id)
#     if not blog.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"Blog with the id={id} not found")
#     blog.delete(synchronize_session=False)
#     db.commit()

#     return "done"


# # updating blog with id
# @app.put("/blog/{id}", status_code=status.HTTP_202_ACCEPTED, tags=['blogs'])
# def updateBlogWithId(id, request: schemas.Blog, db: Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id)
#     if not blog.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"Blog with the id={id} not found")
#     blog.update({'title': request.title, 'body': request.body},
#                 synchronize_session=False)
#     db.commit()

#     return f"updation of blog with id= {id} done"



# # create user
# @app.post("/user", response_model=schemas.ShowUser, tags=['users'])
# def createUser(request: schemas.User, db: Session = Depends(get_db)):

#     new_user = models.User(
#         name=request.name, email=request.email, password=Hash.bcrpt(request.password))
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)

#     return new_user


# # getting all users from table
# @app.get("/user", response_model=List[schemas.ShowUser], tags=['users'])
# def getAllUser(db: Session = Depends(get_db)):
#     users = db.query(models.User).all()
#     return users

# # getting user with id from table


# @app.get("/user/{id}", response_model=schemas.ShowUser, tags=['users'])
# def getUserWithId(id: int, db: Session = Depends(get_db)):
#     user = db.query(models.User).filter(models.User.id == id).first()
#     if (user == None):
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"User with the id={id} not found")
#     return user


#  uvicorn Blog.main:app --reload    from root folder
