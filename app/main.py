from fastapi import FastAPI

from app import models
from .router import user, auth, product
from .database import engine

app = FastAPI()

models.Base.metadata.create_all(bind=engine)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(product.router)


@app.get("/")
def root():
    return {"hello": "hello"}
