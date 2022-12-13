from .types import *

# todo: how strawberry unions works?

AddUserResponse = strawberry.union("AddUserResponse", (UserAdded, UserExists))
GetUsersResponse = strawberry.union("GetUsersResponse", (User, UsersNotFound))
GetUserByIdResponse = strawberry.union("GetUserByIdResponse", (User, UsersNotFound, UserIdMissing))
GetUserByEmailResponse = strawberry.union("GetUserByEmailResponse", (User, UsersNotFound, UserEmailMissing))
DeleteUserResponse = strawberry.union("DeleteUserResponse", (UserUpdated, UserNotFound, UserIdMissing))
UpdateUserResponse = strawberry.union("UpdateUserResponse", (UserDeleted, UserNotFound, UserIdMissing))
