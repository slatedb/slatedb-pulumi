import pulumi_discord


def assign_committer_role(user: str):
    pulumi_discord.MemberRoles(
        f"assign_committer_role_{user}",
        # 1232385660460204122 is the server ID for the "SlateDB" server
        server_id="1232385660460204122",
        user_id=user,
        roles=[
            # 1303423411908903005 is the role ID for the "committer" role
            {"role_id": "1303423411908903005"},
        ]
    )
