import pulumi_github


def add_org_owner(username: str):
    pulumi_github.Membership("add_org_owner_{}".format(username),
        username=username,
        role="admin",
    )

def add_repo_owner(username: str, repository: str):
    pulumi_github.RepositoryCollaborator("add_repo_owner_{}_{}".format(repository, username),
        repository=repository,
        username=username,
        permission="admin",
    )
