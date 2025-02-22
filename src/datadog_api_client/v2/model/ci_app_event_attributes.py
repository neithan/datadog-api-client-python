# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.tags_event_attribute import TagsEventAttribute


class CIAppEventAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.tags_event_attribute import TagsEventAttribute

        return {
            "attributes": (
                {
                    str: (
                        bool,
                        date,
                        datetime,
                        dict,
                        float,
                        int,
                        list,
                        str,
                        none_type,
                    )
                },
            ),
            "service": (str,),
            "tags": (TagsEventAttribute,),
            "timestamp": (datetime,),
        }

    attribute_map = {
        "attributes": "attributes",
        "service": "service",
        "tags": "tags",
        "timestamp": "timestamp",
    }

    def __init__(
        self_,
        attributes: Union[Dict[str, Any], UnsetType] = unset,
        service: Union[str, UnsetType] = unset,
        tags: Union[TagsEventAttribute, UnsetType] = unset,
        timestamp: Union[datetime, UnsetType] = unset,
        **kwargs,
    ):
        """
        JSON object containing all event attributes and their associated values.

        :param attributes: JSON object of attributes from CI Visibility events.
        :type attributes: {str: (bool, date, datetime, dict, float, int, list, str, none_type,)}, optional

        :param service: The name of the application or service generating CI Visibility events.
            It is used to switch from CI Visibility to APM, so make sure you define the same
            value when you use both products.
        :type service: str, optional

        :param tags: Array of tags associated with your event.
        :type tags: TagsEventAttribute, optional

        :param timestamp: Timestamp of your event.
        :type timestamp: datetime, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if service is not unset:
            kwargs["service"] = service
        if tags is not unset:
            kwargs["tags"] = tags
        if timestamp is not unset:
            kwargs["timestamp"] = timestamp
        super().__init__(kwargs)
