import os
from .repo import UserRepository

def get_repo():
    dsn = os.getenv("USER_REGISTRY_DSN")

    if not dsn:
        raise RuntimeError("config error: set USER_REGISTRY_DSN environment variable")

    return UserRepository(dsn)

