from uplink import (
    get,
    Path,
    Consumer,
)

from serverless_wsgi.settings import settings


class GitHub(Consumer):
    """A Client for the GitHub API."""

    @get('/users/{user}')
    def get_user(self, user: Path):
        """Retrieves the user information."""


    @get('/users/{user}/repos')
    def get_repos(self, user: Path):
        """Retrieves the user's public repositories."""


github = GitHub(base_url=settings.GITHUB_PUBLIC_API)
