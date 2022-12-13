from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

import strawberry
from strawberry.fastapi import GraphQLRouter

from db_lib import crud, models, schemas
from db_lib.database import SessionLocal, engine
from graphql_lib.query import Query
from graphql_lib.mutation import Mutation
from graphql_lib.types import strawberry_sqlalchemy_mapper

import uvicorn


models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    middleware=[
        Middleware(
            CORSMiddleware,
            allow_origins=['*'],
            allow_credentials=True,
            allow_methods=['*'],
            allow_headers=['*']
        )
    ]
)

strawberry_sqlalchemy_mapper.finalize()
# additional_types = list(strawberry_sqlalchemy_mapper.mapped_types.values())

schema = strawberry.Schema(
    query=Query,
    mutation=Mutation,
)
graphql_app = GraphQLRouter(schema)

app.include_router(
    graphql_app,
    prefix="/graphql"
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/health')
async def status():
    return JSONResponse({"message": "Health check passed!"}, status_code=200)


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.add_user(db=db, user=user)
    if db_user.id == -1:
        raise HTTPException(status_code=400, detail=f"Email: {user.email} already registered")

    return db_user


@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)

    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user_by_id(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail=f"User not found with id: {user_id}")

    return db_user


@app.get("/users/{email}", response_model=schemas.User)
def read_user_by_email(email: str, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=email)
    if db_user is None:
        raise HTTPException(status_code=404, detail=f"User not found with email: {email}")

    return db_user


@app.put("/users/", response_model=schemas.User)
def update_user(user: schemas.UserUpdated, db: Session = Depends(get_db)):
    db_user = crud.update_user(db, user=user)
    if db_user.id == -1:
        raise HTTPException(status_code=404, detail=f"User not found with id: {user.id}")

    return db_user


@app.delete("/users/{user_id}", response_model=schemas.User)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.delete_user(db, user_id=user_id)
    if db_user.id == -1:
        raise HTTPException(status_code=404, detail=f"User not found with id: {user_id}")

    return db_user


if __name__ == '__main__':
    uvicorn.run("app:app", host='localhost', port=8000, reload=True)
