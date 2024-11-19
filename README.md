# slatedb-pulumi

Pulumi scripts to manage SlateDB committer access to:

- Github
- Discord
- Crates.io

Users must still be manually added to [SlateDB's Pulumi cloud organization](https://app.pulumi.com/slatedb/members). The Pulumi state is stored in Pulumi Cloud. The state is stored in the `slatedb` organization. The state is stored in the `slatedb-pulumi/prod` stack.

## Environment Variables

The following environment variables must be set:

### `PULUMI_ACCESS_TOKEN`

A Pulumi Cloud access token is used to authenticate with Pulumi Cloud. The Pulumi access token can be created in the [organization access tokens](https://app.pulumi.com/slatedb/settings/org-tokens) page.

### `CARGO_REGISTRY_TOKEN`

Can be created from https://crates.io/settings/tokens.

### `DISCORD_TOKEN`

Can be created from https://discord.com/developers. The Github actions in this repository use [@criccomini](https://github/criccomini)'s Discord bot. If you ever need to create your own Discord bot, you can do so by following these instructions:

1. Create a Discord bot. (follow [these inscrutions](https://discordpy.readthedocs.io/en/stable/discord.html))
2. Add the discord bot to SlateDB with the appropriate permissions. (follow [these instructions](https://stackoverflow.com/questions/50942405/discord-js-unknown-guild-when-removing-all-roles-from-a-user))

### `GITHUB_TOKEN`

Can be created from https://github.com/settings/tokens?type=beta.

The Github actions in this repository use [@criccomini](https://github/criccomini)'s personal access token to grant users access to the `slatedb` Github organization. (Github does not allow the use of Github tokens in Github actions to grant users access to an organization.)
