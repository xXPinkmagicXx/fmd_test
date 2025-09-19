class RequestInfo:
    """
    RequestInfo is a class that represents the information of a request.
    """

    def __init__(
            self,
            github_token: str,
            repo_owner: str,
            repo_name: str,
            endpoint: str):
        """
        Initializes the RequestInfo object with the given parameters.

        """
        self.repo_owner = repo_owner
        self.repo_name = repo_name
        self.github_token = github_token
        self.endpoint = endpoint 