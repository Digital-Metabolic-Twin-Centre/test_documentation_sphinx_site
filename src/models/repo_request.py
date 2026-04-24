from pydantic import BaseModel


class RepoRequest(BaseModel):
    """
    """Represents a request for repository information.
    
        Args:
            provider (str): The repository provider, either 'github' or 'gitlab'.
            repo_url (str): The URL of the repository.
            token (str): Authentication token for accessing the repository.
            branch (str): The branch of the repository to access.
    
        Returns:
            None
        """
    """
    provider: str  # "github" or "gitlab"
    repo_url: str
    token: str
    branch: str
