from github_api import get_repos, get_user_repos, get_specific_repo

def list_org_repos(org, token):
    return get_repos(org, token)

def list_user_repos(username, token):
    return get_user_repos(username, token)

def list_specific_repo(username, repo, token):
    return get_specific_repo(username, repo, token)