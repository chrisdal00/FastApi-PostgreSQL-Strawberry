from sqlalchemy.orm import Session
from . import models, schemas


def create_user(name: str = None, email: str = None, password: str = None):
    return schemas.UserCreate(
        name=name,
        email=email,
        password=password
    )


def create_user_to_update(user_id: int, name: str = None, email: str = None, password: str = None):
    return schemas.UserUpdated(
        id=user_id,
        name=name,
        email=email,
        password=password
    )


def hash_password(password: str):
    return password + 'not really hashed'


def add_user(db: Session, user: schemas.UserCreate):
    existing_user = db.query(models.User).filter(models.User.email == user.email).first()

    if existing_user is not None:
        return models.User(id=-1, email=existing_user.email, name=existing_user.name, password=existing_user.password)

    fake_hashed_password = hash_password(user.password)
    db_user = models.User(email=user.email, name=user.name, password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def update_user(db: Session, user: schemas.UserUpdated):
    existing_user = db.query(models.User).filter(models.User.id == user.id).first()

    if existing_user is None:
        return models.User(id=-1, email="", name="", password="")

    # Update only specific fields if len(attribute) > 0
    existing_user.email = user.email if len(user.email) > 0 else existing_user.email
    existing_user.name = user.name if len(user.name) > 0 else existing_user.name
    existing_user.password = hash_password(user.password) if len(user.password) > 0 else existing_user.password

    db.commit()
    db.refresh(existing_user)

    return existing_user


def delete_user(db: Session, user_id: int):
    if db.query(models.User).filter(models.User.id == user_id).delete() == 1:
        db.commit()
        return user_id

    else:
        return -1


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()  # or fetch_one


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()  # or fetch_one


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()  # or fetch_all
