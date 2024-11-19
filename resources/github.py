import pulumi_github


def add_org_owner(username: str):
    pulumi_github.Membership(f"add_github_org_owner_{username}",
        username=username,
        role="admin",
    )


def add_repo_owner(username: str, repository: str):
    pulumi_github.RepositoryCollaborator(f"add_github_repo_owner_{repository}_{username}",
        repository=repository,
        username=username,
        permission="admin",
    )
