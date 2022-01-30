from mangum import Mangum
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers.api import api
from .settings import settings


app = FastAPI(
    title=settings.APP_SETTINGS.PROJECT_NAME,
    description=settings.APP_SETTINGS.PROJECT_DESCRIPTION,
    version=settings.APP_SETTINGS.PROJECT_VERSION,
    debug=settings.DEBUG,
    docs_url=f"{settings.API_PREFIX}/docs",
    openapi_url=f"{settings.API_PREFIX}/openapi.json",
)

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api, prefix=f"{settings.API_PREFIX}")
handler = Mangum(app=app)
