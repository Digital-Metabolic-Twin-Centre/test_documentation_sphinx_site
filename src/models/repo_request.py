from pydantic import BaseModel


class RepoRequest(BaseModel):
    """
    A model representing a repository request with provider details.

    Args:
        provider (str): The version control provider, either 'github' or 'gitlab'.
        repo_url (str): The URL of the repository.
        token (str): Access token for authentication.
        branch (str): The branch of the repository.

    Returns:
        None

    """

    provider: str  # "github" or "gitlab"
    repo_url: str
    token: str
    branch: str
