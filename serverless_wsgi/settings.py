import toml
from pydantic import (
    BaseSettings,
    BaseModel,
    Field,
)

import os
from typing import Optional


class AppSettings(BaseModel):
    """Application settings."""

    PROJECT_NAME: str = None
    PROJECT_VERSION: str = None
    PROJECT_DESCRIPTION: str = None

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    def __init__(self, *args, **kwargs) -> None:
        super().__init__()

        with open(os.path.join(self.BASE_DIR, 'pyproject.toml')) as f:
            package_info = toml.load(f)

        self.PROJECT_NAME = package_info['tool']['poetry']['name']
        self.PROJECT_VERSION = package_info['tool']['poetry']['version']
        self.PROJECT_DESCRIPTION = package_info['tool']['poetry']['description']


class GlobalSettings(BaseSettings):
    """Global settings."""

    APP_SETTINGS: AppSettings = AppSettings()

    DEBUG: Optional[bool] = Field(True, env='DEBUG')
    API_PREFIX: Optional[str] = Field('/serverless-wsgi', env='API_PREFIX')

    GITHUB_PUBLIC_API: Optional[str] = 'https://api.github.com'


settings = GlobalSettings()
