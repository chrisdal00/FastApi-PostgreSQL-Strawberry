from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False, unique=True, index=True)
    password = Column(String(250), nullable=False)
