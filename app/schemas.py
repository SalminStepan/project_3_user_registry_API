from datetime import datetime
from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    phone: str
    city: str

class UserResponse(BaseModel):
    id: int
    name: str
    phone: str
    city: str
    created_at: datetime

class UsersPage(BaseModel):
    items: list[UserResponse]
    limit: int
    offset: int

class UserUpdate(BaseModel):
    name: str | None = None
    phone: str | None = None
    city: str | None = None
