from fastapi import Depends, status, HTTPException,APIRouter
from .. import schemas, models,database
from sqlalchemy.orm import Session
from typing import List
from ..repository import blog
from ..oauth2 import oauth2_scheme

router=APIRouter(
    tags=['Blogs'],
    prefix="/blog"
)


# getting all blogs from table
@router.get("/", response_model=List[schemas.ShowBlog])
def getAllBlog(db: Session = Depends(database.get_db),current_user:schemas.User=Depends(oauth2_scheme)):
    return blog.getAllBlogs(db)


# posting blogs
@router.post("/", status_code=status.HTTP_201_CREATED)
def createBlog(request: schemas.Blog, db: Session = Depends(database.get_db),current_user:schemas.User=Depends(oauth2_scheme)):
    return blog.addBlog(request,db)

# getting blog with id from table
@router.get("/{id}", status_code=200, response_model=schemas.ShowBlog)
def getBlogWithId(id, db: Session = Depends(database.get_db),current_user:schemas.User=Depends(oauth2_scheme)):
    return blog.getBlog(id,db)

# deleting blog with id
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def deleteBlogWithId(id, db: Session = Depends(database.get_db),current_user:schemas.User=Depends(oauth2_scheme)):
   return blog.deleteBlog(id,db);


# updating blog with id
@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def updateBlogWithId(id, request: schemas.Blog, db: Session = Depends(database.get_db),current_user:schemas.User=Depends(oauth2_scheme)):
    return blog.updateBlog(id,request,db);