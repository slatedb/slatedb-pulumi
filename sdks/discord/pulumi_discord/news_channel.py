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

__all__ = ['NewsChannelArgs', 'NewsChannel']

@pulumi.input_type
class NewsChannelArgs:
    def __init__(__self__, *,
                 server_id: pulumi.Input[str],
                 category: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 position: Optional[pulumi.Input[float]] = None,
                 sync_perms_with_category: Optional[pulumi.Input[bool]] = None,
                 topic: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a NewsChannel resource.
        :param pulumi.Input[str] server_id: ID of server this channel is in.
        :param pulumi.Input[str] category: ID of category to place this channel in.
        :param pulumi.Input[str] name: Name of the channel.
        :param pulumi.Input[float] position: Position of the channel, `0`-indexed.
        :param pulumi.Input[bool] sync_perms_with_category: Whether channel permissions should be synced with the category this channel is in.
        :param pulumi.Input[str] topic: Topic of the channel.
        :param pulumi.Input[str] type: The type of the channel. This is only for internal use and should never be provided.
        """
        pulumi.set(__self__, "server_id", server_id)
        if category is not None:
            pulumi.set(__self__, "category", category)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if position is not None:
            pulumi.set(__self__, "position", position)
        if sync_perms_with_category is not None:
            pulumi.set(__self__, "sync_perms_with_category", sync_perms_with_category)
        if topic is not None:
            pulumi.set(__self__, "topic", topic)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="serverId")
    def server_id(self) -> pulumi.Input[str]:
        """
        ID of server this channel is in.
        """
        return pulumi.get(self, "server_id")

    @server_id.setter
    def server_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "server_id", value)

    @property
    @pulumi.getter
    def category(self) -> Optional[pulumi.Input[str]]:
        """
        ID of category to place this channel in.
        """
        return pulumi.get(self, "category")

    @category.setter
    def category(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "category", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the channel.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def position(self) -> Optional[pulumi.Input[float]]:
        """
        Position of the channel, `0`-indexed.
        """
        return pulumi.get(self, "position")

    @position.setter
    def position(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "position", value)

    @property
    @pulumi.getter(name="syncPermsWithCategory")
    def sync_perms_with_category(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether channel permissions should be synced with the category this channel is in.
        """
        return pulumi.get(self, "sync_perms_with_category")

    @sync_perms_with_category.setter
    def sync_perms_with_category(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "sync_perms_with_category", value)

    @property
    @pulumi.getter
    def topic(self) -> Optional[pulumi.Input[str]]:
        """
        Topic of the channel.
        """
        return pulumi.get(self, "topic")

    @topic.setter
    def topic(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "topic", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of the channel. This is only for internal use and should never be provided.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)


@pulumi.input_type
class _NewsChannelState:
    def __init__(__self__, *,
                 category: Optional[pulumi.Input[str]] = None,
                 channel_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 position: Optional[pulumi.Input[float]] = None,
                 server_id: Optional[pulumi.Input[str]] = None,
                 sync_perms_with_category: Optional[pulumi.Input[bool]] = None,
                 topic: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering NewsChannel resources.
        :param pulumi.Input[str] category: ID of category to place this channel in.
        :param pulumi.Input[str] channel_id: The ID of the channel.
        :param pulumi.Input[str] name: Name of the channel.
        :param pulumi.Input[float] position: Position of the channel, `0`-indexed.
        :param pulumi.Input[str] server_id: ID of server this channel is in.
        :param pulumi.Input[bool] sync_perms_with_category: Whether channel permissions should be synced with the category this channel is in.
        :param pulumi.Input[str] topic: Topic of the channel.
        :param pulumi.Input[str] type: The type of the channel. This is only for internal use and should never be provided.
        """
        if category is not None:
            pulumi.set(__self__, "category", category)
        if channel_id is not None:
            pulumi.set(__self__, "channel_id", channel_id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if position is not None:
            pulumi.set(__self__, "position", position)
        if server_id is not None:
            pulumi.set(__self__, "server_id", server_id)
        if sync_perms_with_category is not None:
            pulumi.set(__self__, "sync_perms_with_category", sync_perms_with_category)
        if topic is not None:
            pulumi.set(__self__, "topic", topic)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def category(self) -> Optional[pulumi.Input[str]]:
        """
        ID of category to place this channel in.
        """
        return pulumi.get(self, "category")

    @category.setter
    def category(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "category", value)

    @property
    @pulumi.getter(name="channelId")
    def channel_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the channel.
        """
        return pulumi.get(self, "channel_id")

    @channel_id.setter
    def channel_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "channel_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the channel.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def position(self) -> Optional[pulumi.Input[float]]:
        """
        Position of the channel, `0`-indexed.
        """
        return pulumi.get(self, "position")

    @position.setter
    def position(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "position", value)

    @property
    @pulumi.getter(name="serverId")
    def server_id(self) -> Optional[pulumi.Input[str]]:
        """
        ID of server this channel is in.
        """
        return pulumi.get(self, "server_id")

    @server_id.setter
    def server_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "server_id", value)

    @property
    @pulumi.getter(name="syncPermsWithCategory")
    def sync_perms_with_category(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether channel permissions should be synced with the category this channel is in.
        """
        return pulumi.get(self, "sync_perms_with_category")

    @sync_perms_with_category.setter
    def sync_perms_with_category(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "sync_perms_with_category", value)

    @property
    @pulumi.getter
    def topic(self) -> Optional[pulumi.Input[str]]:
        """
        Topic of the channel.
        """
        return pulumi.get(self, "topic")

    @topic.setter
    def topic(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "topic", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of the channel. This is only for internal use and should never be provided.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)


class NewsChannel(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 category: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 position: Optional[pulumi.Input[float]] = None,
                 server_id: Optional[pulumi.Input[str]] = None,
                 sync_perms_with_category: Optional[pulumi.Input[bool]] = None,
                 topic: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a NewsChannel resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] category: ID of category to place this channel in.
        :param pulumi.Input[str] name: Name of the channel.
        :param pulumi.Input[float] position: Position of the channel, `0`-indexed.
        :param pulumi.Input[str] server_id: ID of server this channel is in.
        :param pulumi.Input[bool] sync_perms_with_category: Whether channel permissions should be synced with the category this channel is in.
        :param pulumi.Input[str] topic: Topic of the channel.
        :param pulumi.Input[str] type: The type of the channel. This is only for internal use and should never be provided.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: NewsChannelArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a NewsChannel resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param NewsChannelArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(NewsChannelArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 category: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 position: Optional[pulumi.Input[float]] = None,
                 server_id: Optional[pulumi.Input[str]] = None,
                 sync_perms_with_category: Optional[pulumi.Input[bool]] = None,
                 topic: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = NewsChannelArgs.__new__(NewsChannelArgs)

            __props__.__dict__["category"] = category
            __props__.__dict__["name"] = name
            __props__.__dict__["position"] = position
            if server_id is None and not opts.urn:
                raise TypeError("Missing required property 'server_id'")
            __props__.__dict__["server_id"] = server_id
            __props__.__dict__["sync_perms_with_category"] = sync_perms_with_category
            __props__.__dict__["topic"] = topic
            __props__.__dict__["type"] = type
            __props__.__dict__["channel_id"] = None
        super(NewsChannel, __self__).__init__(
            'discord:index/newsChannel:NewsChannel',
            resource_name,
            __props__,
            opts,
            package_ref=_utilities.get_package())

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            category: Optional[pulumi.Input[str]] = None,
            channel_id: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            position: Optional[pulumi.Input[float]] = None,
            server_id: Optional[pulumi.Input[str]] = None,
            sync_perms_with_category: Optional[pulumi.Input[bool]] = None,
            topic: Optional[pulumi.Input[str]] = None,
            type: Optional[pulumi.Input[str]] = None) -> 'NewsChannel':
        """
        Get an existing NewsChannel resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] category: ID of category to place this channel in.
        :param pulumi.Input[str] channel_id: The ID of the channel.
        :param pulumi.Input[str] name: Name of the channel.
        :param pulumi.Input[float] position: Position of the channel, `0`-indexed.
        :param pulumi.Input[str] server_id: ID of server this channel is in.
        :param pulumi.Input[bool] sync_perms_with_category: Whether channel permissions should be synced with the category this channel is in.
        :param pulumi.Input[str] topic: Topic of the channel.
        :param pulumi.Input[str] type: The type of the channel. This is only for internal use and should never be provided.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _NewsChannelState.__new__(_NewsChannelState)

        __props__.__dict__["category"] = category
        __props__.__dict__["channel_id"] = channel_id
        __props__.__dict__["name"] = name
        __props__.__dict__["position"] = position
        __props__.__dict__["server_id"] = server_id
        __props__.__dict__["sync_perms_with_category"] = sync_perms_with_category
        __props__.__dict__["topic"] = topic
        __props__.__dict__["type"] = type
        return NewsChannel(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def category(self) -> pulumi.Output[Optional[str]]:
        """
        ID of category to place this channel in.
        """
        return pulumi.get(self, "category")

    @property
    @pulumi.getter(name="channelId")
    def channel_id(self) -> pulumi.Output[str]:
        """
        The ID of the channel.
        """
        return pulumi.get(self, "channel_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the channel.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def position(self) -> pulumi.Output[Optional[float]]:
        """
        Position of the channel, `0`-indexed.
        """
        return pulumi.get(self, "position")

    @property
    @pulumi.getter(name="serverId")
    def server_id(self) -> pulumi.Output[str]:
        """
        ID of server this channel is in.
        """
        return pulumi.get(self, "server_id")

    @property
    @pulumi.getter(name="syncPermsWithCategory")
    def sync_perms_with_category(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether channel permissions should be synced with the category this channel is in.
        """
        return pulumi.get(self, "sync_perms_with_category")

    @property
    @pulumi.getter
    def topic(self) -> pulumi.Output[Optional[str]]:
        """
        Topic of the channel.
        """
        return pulumi.get(self, "topic")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[Optional[str]]:
        """
        The type of the channel. This is only for internal use and should never be provided.
        """
        return pulumi.get(self, "type")

