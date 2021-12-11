from .. import models, schemas, utility
from fastapi import FastAPI, Response, responses, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm.session import Session
from ..database import *

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def Create_User(user: schemas.UserCreate, db: Session = Depends(get_db)):

    password = utility.hash(user.password)
    user.password = password
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get("/{id}", response_model=schemas.UserOut)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id: {id} was not found")
    return user
