# holds user path operations
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from .. import models, schemas, utils
from ..database import get_db

# adding router so router. works
router = APIRouter(prefix="/users", tags=["Users"])


# path operation for user auth
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # hashing user password
    hashed_password = utils.hash(user.password)
    user.password = hashed_password
    new_user = models.User(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


# getting a user with id
@router.get("/{id}", response_model=schemas.UserOut)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        utils.user_raise_404(id)
    return user
