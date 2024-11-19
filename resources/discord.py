import pulumi_discord


def assign_committer_role(user: str):
    pulumi_discord.MemberRoles(
        f"assign_discord_committer_role_{user}",
        server_id="SlateDB",
        user_id=user,
        roles=[
            # 1303423411908903005 is the role ID for the "committer" role
            {"role_id": "1303423411908903005"},
        ]
    )
