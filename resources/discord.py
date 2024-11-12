import pulumi_discord

def assign_committer_role(user: str):
    pulumi_discord.MemberRoles(
        f"assign_committer_role_{user}",
        server_id="1232385660460204122",
        user_id=user,
        roles=[
            {"role_id": "1303423411908903005"},
        ]
    )
