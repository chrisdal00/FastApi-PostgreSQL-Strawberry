from .types import *
from src.db_lib import crud, models
from src.db_lib.database import SessionLocal, engine
from pydantic.typing import List
import strawberry


models.Base.metadata.create_all(bind=engine)
db = SessionLocal()


@strawberry.type
class Query:

    @strawberry.field
    def get_users(self, skip: int, limit: int) -> List[User]:
        return crud.get_users(db, skip=skip, limit=limit)

    @strawberry.field
    def get_user_by_id(self, user_id: int) -> User:
        user = crud.get_user(db, user_id=user_id)
        if user is None:
            raise Exception(f"Cannot find user with id: {user_id}")

        return user

    @strawberry.field
    def get_user_by_email(self, email: str) -> User:
        user = crud.get_user_by_email(db, email=email)
        if user is None:
            raise Exception(f"Cannot find user with email: {email}")

        return user
