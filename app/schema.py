import datetime
from typing import Literal, List
import uuid

from pydantic import BaseModel


class IdReturnBase(BaseModel):
    id: int


class StatusSuccessBase(BaseModel):
    status: Literal["success"]


class GetAdvResponse(BaseModel):

    id: int
    title: str
    description: str
    price: float
    author: int
    create_date: datetime.datetime


class CreateAdvRequest(BaseModel):

    title: str
    description: str
    price: float


class CreateAdvResponse(IdReturnBase):
    pass


class UpdateAdvRequest(BaseModel):

    title: str | None = None
    description: str | None = None
    price: float | None = None


class UpdateAdvResponse(IdReturnBase):
    pass


class DeleteAdvResponse(StatusSuccessBase):
    pass


class SearchAdvResponse(BaseModel):

    result: List[GetAdvResponse]


class BaseUser(BaseModel):

    name: str
    password: str


class LoginRequest(BaseUser):
    pass


class LoginResponse(BaseModel):
    token: uuid.UUID


class CreateUserRequest(BaseUser):

    role: Literal['admin'] | None = None


class CreateUserResponse(IdReturnBase):
    pass


class GetUserResponse(BaseModel):

    id: int
    name: str
    advs: List[GetAdvResponse]


class UpdateUserRequest(BaseModel):

    name: str | None = None
    password: str | None = None


class UpdateUserResponse(IdReturnBase):
    pass


class DeleteUserResponse(StatusSuccessBase):
    pass
