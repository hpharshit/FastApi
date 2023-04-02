from fastapi import Depends, status, HTTPException, APIRouter
from .. import schemas, models, database
from sqlalchemy.orm import Session
from typing import List
from ..repository import user


router = APIRouter(
    tags=['Users'],
    prefix="/user"
)


# create user
@router.post("/", response_model=schemas.ShowUser)
def createUser(request: schemas.User, db: Session = Depends(database.get_db)):
    return user.addUser(request, db)


# getting all users from table
@router.get("/", response_model=List[schemas.ShowUser])
def getAllUser(db: Session = Depends(database.get_db)):
    return user.allUser(db)

# getting user with id from table


@router.get("/{id}", response_model=schemas.ShowUser)
def getUserWithId(id: int, db: Session = Depends(database.get_db)):
    return user.getUser(id,db);
