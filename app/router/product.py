from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..database import get_db
from .. import models, schema
from .. import oauth2

router = APIRouter(prefix="/products", tags=["Products"])


# @router.get("/")
# def read_products(
#     db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)
# ):
#     products = db.query(models.Product).all()
#     if not products:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND, detail="No products found"
#         )
#     return products.__dict__


# @router.get("/{id}")
# def read_products_by_id(
#     db: Session = Depends(get_db),
#     current_user: int = Depends(oauth2.get_current_user),
# ):
#     products = db.query(models.Product).filter(models.Product.id == id).first()
#     if not products:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND, detail="No products found"
#         )

#     return products.__dict__


@router.post("/", response_model=schema.ProductResponse)
def create_product(
    id: int,
    product: schema.ProductCreate,
    db: Session = Depends(get_db),
):
    product.owner_id = id
    new_product = models.Product(**product.dict())

    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return new_product
