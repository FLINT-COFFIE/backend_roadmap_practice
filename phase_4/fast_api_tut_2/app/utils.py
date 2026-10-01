# holds utility functions
from fastapi import HTTPException, status
from passlib.context import CryptContext

# hashing password
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# hash function
def hash(password: str):
    return pwd_context.hash(password)


# verify hash function
def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


# raise 404
# error post
def post_raise_404(id):
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"post with id {id} was not found",
    )


def user_raise_404(id):
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"user with id {id} was not found",
    )


def auth_raise_403():
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="invalid user credentials",
    )


def modify_raise_403():
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Not authorised to perform requested action.",
    )
