from github_api import get_workflow_permissions_in_org

def copy_workflow_permissions(source_org, target_org, repo_name, token):
    rules = get_workflow_permissions_in_org(source_org, repo_name, token)
