from fastapi import APIRouter, HTTPException, status
from fastapi import Depends, APIRouter
from .. import schemas, database, models
from fastapi.security import  OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from ..hashing import Hash
from ..token import create_access_token

router = APIRouter(
    tags=['Authentication'],
    prefix="/login"
)


@router.post("/")
def login(request: OAuth2PasswordRequestForm=Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(
        models.User.email == request.username).first()

    # incorrect email-id
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Incorrect email id = {request.username} ")

    # incorrect password
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Incorrect password = {request.password}")

    # generate jwt token
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

    return user
