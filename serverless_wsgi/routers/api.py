from fastapi import APIRouter

from . import github


api = APIRouter()


api.include_router(github.router, prefix='/github', tags=['GitHub API'])
