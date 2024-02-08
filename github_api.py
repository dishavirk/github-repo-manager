import requests

# generic api function
def api_request(method, url, token, data=None):
    headers = {"Authorization": f"Bearer {token}"}
    if method == 'get':
        response = requests.get(url, headers=headers)
    elif method == 'post':
        response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    return response.json()

# get list of GitHub repos from organisation
def get_repos(org, token):
    url = f"https://api.github.com/repos/{org}/repos"
    return api_request('get', url, token)

# get list of GitHub repos for a user
def get_user_repos(username, token):
    url = f"https://api.github.com/users/{username}/repos"
    return api_request('get', url, token)

def get_specific_repo(username, repo, token):
    url = f"https://api.github.com/repos/{username}/{repo}"
    return api_request('get', url, token)

#  get branch protection rules for a repo
def get_branch_protection(org, repo, token):
    url = f"https://api.github.com/repos/{org}/{repo}/branches/main/protection"
    return api_request('get', url, token)

# set branch protection rules for a repo
def set_branch_protection(org, repo, rules, token):
    url = f"https://api.github.com/repos/{org}/{repo}/branches/main/protection"
    return api_request('post', url, token, data=rules)

def get_workflow_permissions_in_org(org, repo, token):
    url = f" https://api.github.com/repos/{org}/{repo}/actions/permissions"

