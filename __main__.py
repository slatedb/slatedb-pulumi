"""
This is the main entry point for SlateDB's Pulumi configuration. It manages
memberships and permissions for SlateDB's open source resources such as
Github, Discord, and Crates.io.
"""

from dataclasses import dataclass

from resources import crates, discord, github

@dataclass
class Maintainer:
    name: str
    github: str
    discord: str


MAINTAINERS = [
    Maintainer(
        name="Chris Riccomini",
        github="criccomini",
        discord="839536195603922974",
    ),
    Maintainer(
        name="Rohan Desai",
        github="rodesai",
        discord="1144686022010097794",
    ),
    Maintainer(
        name="Vignesh Chandramohan",
        github="vigneshc",
        discord="894942567513337887",
    ),
    Maintainer(
        name="Paul Butler",
        github="paulgb",
        discord="534035699565854720",
    ),
    Maintainer(
        name="Li Yazhou",
        github="flaneur2020",
        discord="965845316370833408",
    ),
    Maintainer(
        name="Almog Gavra",
        github="agavra",
        discord="1154560747330867221",
    ),
    Maintainer(
        name="David Moravek",
        github="dmvk",
        discord="1301098116228845620",
    ),
    Maintainer(
        name="Jason Gustafson",
        github="hachikuji",
        discord="1290758620664827966",
    ),
]


def main():
    for maintainer in MAINTAINERS:
        github.add_org_owner(maintainer.github)
        discord.assign_committer_role(maintainer.discord)
        crates.add_owner(maintainer.github, "slatedb")
        crates.add_owner(maintainer.github, "fail-parallel")

    # Outside collaborators for slatedb-go
    github.add_repo_owner("naveen246", "slatedb-go")
    github.add_repo_owner("thrawn01", "slatedb-go")


if __name__ == "__main__":
    main()
