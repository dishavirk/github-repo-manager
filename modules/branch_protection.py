from github_api import get_branch_protection, set_branch_protection

def copy_branch_protection_rules(source_org, target_org, repo_name, token):
    rules = get_branch_protection(source_org, repo_name, token)
    set_branch_protection(target_org, repo_name, rules, token)
