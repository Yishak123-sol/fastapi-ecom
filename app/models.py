from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, func
from .database import Base
from sqlalchemy.orm import relationship

""" --------------  User Table  ------------------------------------ """


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(String, default="CUSTOMER")
    created_at = Column(DateTime(timezone=True), server_default=func.now())


""" --------------  Product Table  ------------------------------------ """


class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    stock = Column(Integer, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    owner_id = Column(
        Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    owner = relationship("User")
