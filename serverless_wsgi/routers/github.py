from fastapi.responses import JSONResponse
from fastapi import (
    Path,
    APIRouter,
)

from serverless_wsgi.controllers.github import github


router = APIRouter()


@router.get('/{user}', summary=github.get_user.__doc__)
def get_github_user(user: str = Path(..., description='GitHub username.')):
    response = github.get_user(user=user)

    return JSONResponse(
        status_code=response.status_code,
        content=response.json()
    )


@router.get('/{user}/repos', summary=github.get_repos.__doc__)
def get_github_user_repos(user: str = Path(..., description='GitHub username.')):
    response = github.get_repos(user=user)

    return JSONResponse(
        status_code=response.status_code,
        content=response.json()
    )
