from typing import Annotated
from fastapi import APIRouter
from fastapi import Depends, HTTPException, status
from app.database import get_db
from sqlalchemy.orm import Session
from .. import models, schema
from .. import utils
from .. import oauth2

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/")
def create_user(
    user_data: schema.User,
    db: Session = Depends(get_db),
):
    hashed_password = utils.hash(user_data.hashed_password)
    user_data.hashed_password = hashed_password

    user = models.User(**user_data.model_dump())
    db.add(user)
    db.commit()
    db.refresh(user)

    return user


@router.get("/{user_id}")
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )

    return user
