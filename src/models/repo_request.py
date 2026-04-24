from pydantic import BaseModel


class RepoRequest(BaseModel):
    """
    A model representing a repository request with provider details.

    Args:
        provider (str): The version control provider ('github' or 'gitlab').
        repo_url (str): The URL of the repository.
        token (str): Access token for authentication.
        branch (str): The branch name to be accessed.

    Returns:
        None
    """

    provider: str  # "github" or "gitlab"
    repo_url: str
    token: str
    branch: str
