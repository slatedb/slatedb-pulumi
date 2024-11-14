from pulumi_command import local


def add_owner(username: str, crate: str):
        add_owner_command = local.Command(
        f"add_owner_{username}",
        create=f"cargo owner --add {username} {crate}",
        delete=f"cargo owner --remove {username} {crate}",
    )
