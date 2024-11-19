# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import sys
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
if sys.version_info >= (3, 11):
    from typing import NotRequired, TypedDict, TypeAlias
else:
    from typing_extensions import NotRequired, TypedDict, TypeAlias
from . import _utilities

__all__ = ['WebhookArgs', 'Webhook']

@pulumi.input_type
class WebhookArgs:
    def __init__(__self__, *,
                 channel_id: pulumi.Input[str],
                 avatar_data_uri: Optional[pulumi.Input[str]] = None,
                 avatar_url: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Webhook resource.
        :param pulumi.Input[str] channel_id: ID of the channel to create a webhook for.
        :param pulumi.Input[str] avatar_data_uri: Data URI of an image to set as the default avatar of the webhook.
        :param pulumi.Input[str] avatar_url: Remote URL for setting the default avatar of the webhook.
        :param pulumi.Input[str] name: Default name of the webhook.
        """
        pulumi.set(__self__, "channel_id", channel_id)
        if avatar_data_uri is not None:
            pulumi.set(__self__, "avatar_data_uri", avatar_data_uri)
        if avatar_url is not None:
            pulumi.set(__self__, "avatar_url", avatar_url)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="channelId")
    def channel_id(self) -> pulumi.Input[str]:
        """
        ID of the channel to create a webhook for.
        """
        return pulumi.get(self, "channel_id")

    @channel_id.setter
    def channel_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "channel_id", value)

    @property
    @pulumi.getter(name="avatarDataUri")
    def avatar_data_uri(self) -> Optional[pulumi.Input[str]]:
        """
        Data URI of an image to set as the default avatar of the webhook.
        """
        return pulumi.get(self, "avatar_data_uri")

    @avatar_data_uri.setter
    def avatar_data_uri(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "avatar_data_uri", value)

    @property
    @pulumi.getter(name="avatarUrl")
    def avatar_url(self) -> Optional[pulumi.Input[str]]:
        """
        Remote URL for setting the default avatar of the webhook.
        """
        return pulumi.get(self, "avatar_url")

    @avatar_url.setter
    def avatar_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "avatar_url", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Default name of the webhook.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _WebhookState:
    def __init__(__self__, *,
                 avatar_data_uri: Optional[pulumi.Input[str]] = None,
                 avatar_hash: Optional[pulumi.Input[str]] = None,
                 avatar_url: Optional[pulumi.Input[str]] = None,
                 channel_id: Optional[pulumi.Input[str]] = None,
                 github_url: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 slack_url: Optional[pulumi.Input[str]] = None,
                 token: Optional[pulumi.Input[str]] = None,
                 url: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Webhook resources.
        :param pulumi.Input[str] avatar_data_uri: Data URI of an image to set as the default avatar of the webhook.
        :param pulumi.Input[str] avatar_hash: Hash of the avatar.
        :param pulumi.Input[str] avatar_url: Remote URL for setting the default avatar of the webhook.
        :param pulumi.Input[str] channel_id: ID of the channel to create a webhook for.
        :param pulumi.Input[str] github_url: The GitHub-compatible webhook URL.
        :param pulumi.Input[str] name: Default name of the webhook.
        :param pulumi.Input[str] slack_url: The Slack-compatible webhook URL.
        :param pulumi.Input[str] token: The webhook token.
        :param pulumi.Input[str] url: The webhook URL.
        """
        if avatar_data_uri is not None:
            pulumi.set(__self__, "avatar_data_uri", avatar_data_uri)
        if avatar_hash is not None:
            pulumi.set(__self__, "avatar_hash", avatar_hash)
        if avatar_url is not None:
            pulumi.set(__self__, "avatar_url", avatar_url)
        if channel_id is not None:
            pulumi.set(__self__, "channel_id", channel_id)
        if github_url is not None:
            pulumi.set(__self__, "github_url", github_url)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if slack_url is not None:
            pulumi.set(__self__, "slack_url", slack_url)
        if token is not None:
            pulumi.set(__self__, "token", token)
        if url is not None:
            pulumi.set(__self__, "url", url)

    @property
    @pulumi.getter(name="avatarDataUri")
    def avatar_data_uri(self) -> Optional[pulumi.Input[str]]:
        """
        Data URI of an image to set as the default avatar of the webhook.
        """
        return pulumi.get(self, "avatar_data_uri")

    @avatar_data_uri.setter
    def avatar_data_uri(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "avatar_data_uri", value)

    @property
    @pulumi.getter(name="avatarHash")
    def avatar_hash(self) -> Optional[pulumi.Input[str]]:
        """
        Hash of the avatar.
        """
        return pulumi.get(self, "avatar_hash")

    @avatar_hash.setter
    def avatar_hash(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "avatar_hash", value)

    @property
    @pulumi.getter(name="avatarUrl")
    def avatar_url(self) -> Optional[pulumi.Input[str]]:
        """
        Remote URL for setting the default avatar of the webhook.
        """
        return pulumi.get(self, "avatar_url")

    @avatar_url.setter
    def avatar_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "avatar_url", value)

    @property
    @pulumi.getter(name="channelId")
    def channel_id(self) -> Optional[pulumi.Input[str]]:
        """
        ID of the channel to create a webhook for.
        """
        return pulumi.get(self, "channel_id")

    @channel_id.setter
    def channel_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "channel_id", value)

    @property
    @pulumi.getter(name="githubUrl")
    def github_url(self) -> Optional[pulumi.Input[str]]:
        """
        The GitHub-compatible webhook URL.
        """
        return pulumi.get(self, "github_url")

    @github_url.setter
    def github_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "github_url", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Default name of the webhook.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="slackUrl")
    def slack_url(self) -> Optional[pulumi.Input[str]]:
        """
        The Slack-compatible webhook URL.
        """
        return pulumi.get(self, "slack_url")

    @slack_url.setter
    def slack_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "slack_url", value)

    @property
    @pulumi.getter
    def token(self) -> Optional[pulumi.Input[str]]:
        """
        The webhook token.
        """
        return pulumi.get(self, "token")

    @token.setter
    def token(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "token", value)

    @property
    @pulumi.getter
    def url(self) -> Optional[pulumi.Input[str]]:
        """
        The webhook URL.
        """
        return pulumi.get(self, "url")

    @url.setter
    def url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "url", value)


class Webhook(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 avatar_data_uri: Optional[pulumi.Input[str]] = None,
                 avatar_url: Optional[pulumi.Input[str]] = None,
                 channel_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a Webhook resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] avatar_data_uri: Data URI of an image to set as the default avatar of the webhook.
        :param pulumi.Input[str] avatar_url: Remote URL for setting the default avatar of the webhook.
        :param pulumi.Input[str] channel_id: ID of the channel to create a webhook for.
        :param pulumi.Input[str] name: Default name of the webhook.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: WebhookArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a Webhook resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param WebhookArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(WebhookArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 avatar_data_uri: Optional[pulumi.Input[str]] = None,
                 avatar_url: Optional[pulumi.Input[str]] = None,
                 channel_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = WebhookArgs.__new__(WebhookArgs)

            __props__.__dict__["avatar_data_uri"] = avatar_data_uri
            __props__.__dict__["avatar_url"] = avatar_url
            if channel_id is None and not opts.urn:
                raise TypeError("Missing required property 'channel_id'")
            __props__.__dict__["channel_id"] = channel_id
            __props__.__dict__["name"] = name
            __props__.__dict__["avatar_hash"] = None
            __props__.__dict__["github_url"] = None
            __props__.__dict__["slack_url"] = None
            __props__.__dict__["token"] = None
            __props__.__dict__["url"] = None
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["githubUrl", "slackUrl", "token", "url"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(Webhook, __self__).__init__(
            'discord:index/webhook:Webhook',
            resource_name,
            __props__,
            opts,
            package_ref=_utilities.get_package())

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            avatar_data_uri: Optional[pulumi.Input[str]] = None,
            avatar_hash: Optional[pulumi.Input[str]] = None,
            avatar_url: Optional[pulumi.Input[str]] = None,
            channel_id: Optional[pulumi.Input[str]] = None,
            github_url: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            slack_url: Optional[pulumi.Input[str]] = None,
            token: Optional[pulumi.Input[str]] = None,
            url: Optional[pulumi.Input[str]] = None) -> 'Webhook':
        """
        Get an existing Webhook resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] avatar_data_uri: Data URI of an image to set as the default avatar of the webhook.
        :param pulumi.Input[str] avatar_hash: Hash of the avatar.
        :param pulumi.Input[str] avatar_url: Remote URL for setting the default avatar of the webhook.
        :param pulumi.Input[str] channel_id: ID of the channel to create a webhook for.
        :param pulumi.Input[str] github_url: The GitHub-compatible webhook URL.
        :param pulumi.Input[str] name: Default name of the webhook.
        :param pulumi.Input[str] slack_url: The Slack-compatible webhook URL.
        :param pulumi.Input[str] token: The webhook token.
        :param pulumi.Input[str] url: The webhook URL.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _WebhookState.__new__(_WebhookState)

        __props__.__dict__["avatar_data_uri"] = avatar_data_uri
        __props__.__dict__["avatar_hash"] = avatar_hash
        __props__.__dict__["avatar_url"] = avatar_url
        __props__.__dict__["channel_id"] = channel_id
        __props__.__dict__["github_url"] = github_url
        __props__.__dict__["name"] = name
        __props__.__dict__["slack_url"] = slack_url
        __props__.__dict__["token"] = token
        __props__.__dict__["url"] = url
        return Webhook(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="avatarDataUri")
    def avatar_data_uri(self) -> pulumi.Output[Optional[str]]:
        """
        Data URI of an image to set as the default avatar of the webhook.
        """
        return pulumi.get(self, "avatar_data_uri")

    @property
    @pulumi.getter(name="avatarHash")
    def avatar_hash(self) -> pulumi.Output[str]:
        """
        Hash of the avatar.
        """
        return pulumi.get(self, "avatar_hash")

    @property
    @pulumi.getter(name="avatarUrl")
    def avatar_url(self) -> pulumi.Output[Optional[str]]:
        """
        Remote URL for setting the default avatar of the webhook.
        """
        return pulumi.get(self, "avatar_url")

    @property
    @pulumi.getter(name="channelId")
    def channel_id(self) -> pulumi.Output[str]:
        """
        ID of the channel to create a webhook for.
        """
        return pulumi.get(self, "channel_id")

    @property
    @pulumi.getter(name="githubUrl")
    def github_url(self) -> pulumi.Output[str]:
        """
        The GitHub-compatible webhook URL.
        """
        return pulumi.get(self, "github_url")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Default name of the webhook.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="slackUrl")
    def slack_url(self) -> pulumi.Output[str]:
        """
        The Slack-compatible webhook URL.
        """
        return pulumi.get(self, "slack_url")

    @property
    @pulumi.getter
    def token(self) -> pulumi.Output[str]:
        """
        The webhook token.
        """
        return pulumi.get(self, "token")

    @property
    @pulumi.getter
    def url(self) -> pulumi.Output[str]:
        """
        The webhook URL.
        """
        return pulumi.get(self, "url")

