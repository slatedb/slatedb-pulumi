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
from .. import _utilities

clientId: Optional[str]
"""
OAuth app client ID. Currently unused.
"""

secret: Optional[str]
"""
OAuth app secret. Currently unused.
"""

token: Optional[str]
"""
Discord API token, without the `Bot` prefix. This can be found in the Discord Developer Portal. This can also be set via
the `DISCORD_TOKEN` environment variable.
"""

