from fastapi import status, HTTPException
from .. import models
from ..hashing import Hash

def addUser(request, db):
    new_user = models.User(
        name=request.name, email=request.email, password=Hash.bcrpt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def allUser(db):
    users = db.query(models.User).all()
    return users


def getUser(id, db):
    user = db.query(models.User).filter(models.User.id == id).first()
    if (user == None):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the id={id} not found")
    return user
