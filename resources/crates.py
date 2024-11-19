from pulumi_command import local


def add_owner(username: str, crate: str):
    local.Command(
        f"add_crate_owner_{username}_{crate}",
        create=(
            f"if ! cargo owner --list {crate} | grep -q {username}; then "
            f"cargo owner --add {username} {crate}; "
            f"else echo 'User {username} is already an owner of {crate}'; "
            f"fi"
        ),
        delete=(
            f"if cargo owner --list {crate} | grep -q {username}; then "
            f"cargo owner --remove {username} {crate}; "
            f"else echo 'User {username} is not an owner of {crate}'; "
            f"fi"
        ),
    )
