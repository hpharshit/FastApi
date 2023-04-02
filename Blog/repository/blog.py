from fastapi import status, HTTPException
from .. import models


def getAllBlogs(db):
    blogs = db.query(models.Blog).all()
    return blogs


def addBlog(request, db):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def getBlog(id, db):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    # returns sqlalchaemy model
    if (blog == None):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with the id={id} not found")
    return blog


def deleteBlog(id, db):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with the id={id} not found")
    blog.delete(synchronize_session=False)
    db.commit()

    return "done"


def updateBlog(id, request,db):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with the id={id} not found")
    blog.update({'title': request.title, 'body': request.body},
                synchronize_session=False)
    db.commit()

    return f"updation of blog with id= {id} done"
