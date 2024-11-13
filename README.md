# slatedb-pulumi

Pulumi scripts to manage SlateDB committer access to various infrastructure resources.

## Pulumi State

The Pulumi state is stored in an S3 bucket called `slatedb-pulumi` stack. [@criccomini](https://github.com/criccomini) created a bucket on Tigris for this purpose. Eventually, we might want to migrate to Pulumi Cloud or AWS S3.

## Environment Variables

The following environment variables must be set:

### `CARGO_REGISTRY_TOKEN`

Can be created from https://crates.io/settings/tokens.

### `DISCORD_TOKEN`

Can be created from https://discord.com/developers.

### `GITHUB_TOKEN`

Can be created from https://github.com/settings/tokens?type=beta.

Github will fill this environment variable in automatically when you run a workflow. Make sure the workflow has the appropriate permissions to grant users ownership of the `slatedb` Github orgnaization and its repositories.