from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from .routers.users import router
from .repositories.users import RepoError, NotFoundError, UniqueViolationError

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok"}

app.include_router(router)

@app.exception_handler(NotFoundError)
async def not_found_handler(request: Request, exc: NotFoundError):
    return JSONResponse(
        status_code=404,
        content={"detail": str(exc)},
    )


@app.exception_handler(UniqueViolationError)
async def unique_violation_handler(request: Request, exc: UniqueViolationError):
    return JSONResponse(
        status_code=409,
        content={"detail": str(exc)},
    )


@app.exception_handler(RepoError)
async def repo_error_handler(request: Request, exc: RepoError):
    return JSONResponse(
        status_code=500,
        content={"detail": "internal database error"},
    )
