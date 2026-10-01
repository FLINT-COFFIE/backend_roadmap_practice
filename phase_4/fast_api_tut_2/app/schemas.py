from datetime import datetime

from pydantic import BaseModel, EmailStr, Field


# making a post base model
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):
    pass


class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True


# response model
class Post(PostBase):
    id: int
    created_at: datetime
    user_id: int
    owner: UserOut

    # converting orm to dict
    class Config:
        # orm_mode=True
        from_attributes = True


class UserCreate(BaseModel):
    # to validate email
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: str | None = None


class Vote(BaseModel):
    post_id: int
    dir: int = Field(ge=0, le=1)


class PostOut(BaseModel):
    Post: Post
    votes: int

    class Config:
        from_attributes = True
