"""
This is the main entry point for SlateDB's Pulumi configuration. It manages
memberships and permissions for SlateDB's open source resources such as
Github, Discord, and Crates.io.
"""

from dataclasses import dataclass

from resources import github

@dataclass
class Maintainer:
    name: str
    github: str
    discord: str
    crates: str


MAINTAINERS = [
    Maintainer(
        name="Chris Riccomini",
        github="criccomini",
        discord="criccomini",
        crates="criccomini",
    ),
    Maintainer(
        name="Rohan Desai",
        github="rodesai",
        discord="",
        crates="",
    ),
    Maintainer(
        name="Vignesh Chandramohan",
        github="vigneshc",
        discord="",
        crates="",
    ),
    Maintainer(
        name="Paul Butler",
        github="paulgb",
        discord="",
        crates="",
    ),
    Maintainer(
        name="Li Yazhou",
        github="flaneur2020",
        discord="",
        crates="",
    ),
]


def main():
    for maintainer in MAINTAINERS:
        github.add_org_owner(maintainer.github)

    # Special case for slatedb-go, which is owned by Naveen right now
    github.add_repo_owner("naveen246", "slatedb-go")


if __name__ == "__main__":
    main()
