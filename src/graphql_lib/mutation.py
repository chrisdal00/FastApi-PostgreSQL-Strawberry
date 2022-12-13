from .types import *
from .fragments import *
from src.db_lib import crud, models
from src.db_lib.database import SessionLocal, engine
import strawberry

models.Base.metadata.create_all(bind=engine)
db = SessionLocal()


@strawberry.type
class Mutation:

    @strawberry.mutation
    def add_user(self, name: str, email: str, password: str) -> UserAdded:
        ret = crud.add_user(
            db=db,
            user=crud.create_user(
                name=name,
                email=email,
                password=password
            )
        )

        if ret.id == -1:
            raise Exception(f"User with email: {email} already exists")

        return UserAdded(id=ret.id)

    @strawberry.mutation
    def update_user(self, user_id: int, name: str, email: str, password: str) -> UserUpdated:
        ret = crud.update_user(
            db=db,
            user=crud.create_user_to_update(
                user_id=user_id,
                name=name,
                email=email,
                password=password
            )
        )

        if ret.id == -1:
            raise Exception(f"User with id: {user_id} not found")

        return UserUpdated(id=ret.id)

    @strawberry.mutation
    def delete_user(self, user_id: int) -> UserDeleted:
        _id = crud.delete_user(
            db=db,
            user_id=user_id
        )

        if _id == -1:
            raise Exception(f"User with id: {user_id} not found")

        return UserDeleted(id=_id)
