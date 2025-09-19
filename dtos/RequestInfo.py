class RequestInfo:
    """
    RequestInfo is a class that represents the information of a request.
    """

    def __init__(self, github_token: str, repo_owner: str, repo_name: str):
        """
        Initializes the RequestInfo object with the given parameters.

        :param method: The HTTP method of the request (e.g., GET, POST).
        :param url: The URL of the request.
        :param headers: The headers of the request.
        :param body: The body of the request.
        """
        self.repo_owner = repo_owner
        self.repo_name = repo_name
        self.github_token = github_token