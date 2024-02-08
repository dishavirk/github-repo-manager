import settings
from modules import repo_management, branch_protection, workflow_permissions

def main():
    try:
        # source_repos = repo_management.list_org_repos(settings.SOURCE_ORG, settings.GITHUB_TOKEN)
        # source_repos = repo_management.list_user_repos(settings.USERNAME, settings.GITHUB_TOKEN)

        # for repo in source_repos:
        #     print(f"Processing repo: {repo['name']}")

        #     branch_protection.copy_branch_protection_rules(settings.SOURCE_ORG, settings.TARGET_ORG, repo['name'], settings.GITHUB_TOKEN)

        #     workflow_permissions.copy_workflow_permissions(settings.SOURCE_ORG, settings.TARGET_ORG, repo['name'], settings.GITHUB_TOKEN)

        specific_repo = repo_management.list_specific_repo(settings.USERNAME, settings.SPECIFIC_REPO, settings.GITHUB_TOKEN)
        print(f"response: {specific_repo}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
