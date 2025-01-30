import datetime
from typing import Annotated
from fastapi import HTTPException, Request, status, Depends, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from app import models
from app.oauth2 import create_access_token
from .. import utils
from ..database import get_db
from sqlalchemy.orm import Session
from ..schema import Token


router = APIRouter(tags=["Authentication"])


@router.post("/token")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: Session = Depends(get_db),
) -> Token:

    error = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect username or password",
        headers={"WWW-Authenticate": "Bearer"},
    )

    user = db.query(models.User).filter(models.User.email == form_data.username).first()
    if not user:
        raise error

    if not utils.verify(form_data.password, user.hashed_password):
        raise error

    access_token_expires = datetime.timedelta(minutes=30)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )

    return Token(access_token=access_token, token_type="bearer").model_dump()
