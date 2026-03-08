from  fastapi import APIRouter, Depends, Query
from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse
from .schemas import UserCreate, UserResponse
from .db import get_repo
from .repo import (
    UserRepository,
    RepoError,
    UniqueViolationError,
    NotFoundError
)


router = APIRouter()

@router.post("/users", response_model=UserResponse)
def create_user(user: UserCreate, repo: UserRepository = Depends(get_repo)):
    created = repo.add_user(user.name, user.phone, user.city)
    return created

@router.get("/users", response_model=list[UserResponse])
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

    return users

@router.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int, repo: UserRepository = Depends(get_repo)):
        user = repo.get_user(user_id)
        return user


@router.delete("/users/{user_id}", response_model=UserResponse)
def delete_user(user_id: int, repo: UserRepository = Depends(get_repo)):
        user = repo.delete_user(user_id)
        return user


@router.put("/users/{user_id}", response_model=UserResponse)
def update_user(
    user_id:int,
    user: UserCreate,
    repo: UserRepository = Depends(get_repo)
):
        updated = repo.update_user(user_id, user.name, user.phone, user.city)
        return updated
