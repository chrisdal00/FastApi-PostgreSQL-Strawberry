import strawberry
from src.db_lib import models
from strawberry_sqlalchemy_mapper import StrawberrySQLAlchemyMapper

strawberry_sqlalchemy_mapper = StrawberrySQLAlchemyMapper()


@strawberry_sqlalchemy_mapper.type(models.User)
class User:
    __exclude__ = ["password"]


@strawberry_sqlalchemy_mapper.type(models.User)
class UserAdded:
    __exclude__ = ["email", "name", "password"]


@strawberry_sqlalchemy_mapper.type(models.User)
class UserUpdated:
    __exclude__ = ["email", "name", "password"]


@strawberry_sqlalchemy_mapper.type(models.User)
class UserDeleted:
    __exclude__ = ["email", "name", "password"]


@strawberry.type
class UserExists:
    message: str = "User with this email already exists"


@strawberry.type
class UserNotFound:
    message: str = "Couldn't find user with the supplied id"


@strawberry.type
class UsersNotFound:
    message: str = "Couldn't find users"


@strawberry.type
class UserNameMissing:
    message: str = "Please supply user name"


@strawberry.type
class UserEmailMissing:
    message: str = "Please supply user email"


@strawberry.type
class UserIdMissing:
    message: str = "Please supply user id"
