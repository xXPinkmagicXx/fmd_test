import requests
from dtos.RequestInfo import RequestInfo 


def get_repo_url(repo_owner:str, repo_name:str):
    return f"https://api.github.com/repos/{repo_owner}/{repo_name}/pulls"    


def make_request(reqest_info: RequestInfo) -> requests.Response:
    # Get the URL for the repository
    url = get_repo_url(reqest_info.repo_owner, reqest_info.repo_name)
    
    # Get headers and params
    headers = get_headers(reqest_info.github_token) # Get headers with token
    params = get_params() # Get defailt params
    
    # Make the request and return the response as a request.Response object
    return requests.get(url, headers=headers, params=params)

def get_params():
    params = { 
        "state": "all",  # Get only open pull requests
    }
    return params


def get_headers(github_token: str):
    headers = {
        "Authorization": f"Bearer {github_token}",
        "Accept": "application/vnd.github.v3+json"
    }
    return headers


def main():
    print("This is a utility file with helper functions not to be run directly.")

if __name__ == "__main__":
    main()