from pydantic import BaseModel, EmailStr

"""-----------------------User Model--------------------------"""


class User(BaseModel):
    email: EmailStr
    hashed_password: str


"""-----------------------Token Model--------------------------"""


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None


"""-----------------------Token Model--------------------------"""


class ProductCreate(BaseModel):
    name: str
    description: str
    price: int
    stock: int
    owner_id: int


class ProductResponse(ProductCreate):
    id: int
    name: str
    price: int
    stock: int

    class Config:
        from_attributes = True
