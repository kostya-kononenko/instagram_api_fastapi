from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    email: str
    password: str


class UserDisplay(BaseModel):
    username: str
    email: str

    class Config:
        from_attributes = True


class User(BaseModel):
    username: str

    class Config:
        from_attributes = True


class UserAuth(BaseModel):
    id: int
    username: str
    email: str
