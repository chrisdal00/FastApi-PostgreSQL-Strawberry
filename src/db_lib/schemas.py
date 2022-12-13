from pydantic import BaseModel


class UserBase(BaseModel):
    id: str
    email: str
    name: str


class UserCreate(BaseModel):
    email: str
    name: str
    password: str


class UserAdded(BaseModel):
    id: int


class UserUpdated(UserBase):
    password: str


class UserDeleted(UserAdded):
    pass


class User(UserBase):
    class Config:
        orm_mode = True
