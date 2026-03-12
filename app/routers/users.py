from fastapi import APIRouter, Depends, Query

from ..schemas.users import UserCreate, UserResponse, UsersPage, UserUpdate
from ..core.db import get_repo
from ..repositories.users import (
    UserRepository,
    RepoError,
    UniqueViolationError,
    NotFoundError
)


router = APIRouter()

@router.post("/users", response_model=UserResponse, status_code=201)
def create_user(user: UserCreate, repo: UserRepository = Depends(get_repo)):
    created = repo.add_user(user.name, user.phone, user.city)
    return created

@router.get("/users", response_model=UsersPage)
def list_users(
    search: str | None = None,
    limit: int = Query(default=10, ge=1, le=100),
    offset:int = Query(default=0, ge=0),
    repo: UserRepository = Depends(get_repo)
):
    if search:
        users = repo.search_users(search, limit, offset)
    else:
        users = repo.list_users(limit, offset)

    return {
        "items": users,
        "limit": limit,
        "offset": offset
    }

@router.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int, repo: UserRepository = Depends(get_repo)):
        user = repo.get_user(user_id)
        return user


@router.delete("/users/{user_id}", response_model=UserResponse)
def delete_user(user_id: int, repo: UserRepository = Depends(get_repo)):
        user = repo.delete_user(user_id)
        return user


@router.patch("/users/{user_id}", response_model=UserResponse)
def update_user(
    user_id:int,
    user: UserUpdate,
    repo: UserRepository = Depends(get_repo)
):
    current = repo.get_user(user_id)
    name = user.name if user.name is not None else current["name"]
    phone = user.phone if user.phone is not None else current["phone"]
    city = user.city if user.city is not None else current["city"]
    updated = repo.update_user(user_id, name, phone, city)
    return updated
