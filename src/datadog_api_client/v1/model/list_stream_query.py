# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v1.model.list_stream_compute_items import ListStreamComputeItems
    from datadog_api_client.v1.model.list_stream_source import ListStreamSource
    from datadog_api_client.v1.model.list_stream_group_by_items import ListStreamGroupByItems


class ListStreamQuery(ModelNormal):
    validations = {
        "compute": {
            "max_items": 5,
            "min_items": 1,
        },
        "group_by": {
            "max_items": 3,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.list_stream_compute_items import ListStreamComputeItems
        from datadog_api_client.v1.model.list_stream_source import ListStreamSource
        from datadog_api_client.v1.model.list_stream_group_by_items import ListStreamGroupByItems

        return {
            "compute": ([ListStreamComputeItems],),
            "data_source": (ListStreamSource,),
            "group_by": ([ListStreamGroupByItems],),
            "indexes": ([str],),
            "query_string": (str,),
            "storage": (str,),
        }

    attribute_map = {
        "compute": "compute",
        "data_source": "data_source",
        "group_by": "group_by",
        "indexes": "indexes",
        "query_string": "query_string",
        "storage": "storage",
    }

    def __init__(
        self_,
        data_source: ListStreamSource,
        query_string: str,
        compute: Union[List[ListStreamComputeItems], UnsetType] = unset,
        group_by: Union[List[ListStreamGroupByItems], UnsetType] = unset,
        indexes: Union[List[str], UnsetType] = unset,
        storage: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Updated list stream widget.

        :param compute: Compute configuration for the List Stream Widget. Compute can be used only with the logs_transaction_stream (from 1 to 5 items) list stream source.
        :type compute: [ListStreamComputeItems], optional

        :param data_source: Source from which to query items to display in the stream.
        :type data_source: ListStreamSource

        :param group_by: Group by configuration for the List Stream Widget. Group by can be used only with logs_pattern_stream (up to 3 items) or logs_transaction_stream (one group by item is required) list stream source.
        :type group_by: [ListStreamGroupByItems], optional

        :param indexes: List of indexes.
        :type indexes: [str], optional

        :param query_string: Widget query.
        :type query_string: str

        :param storage: Option for storage location. Feature in Private Beta.
        :type storage: str, optional
        """
        if compute is not unset:
            kwargs["compute"] = compute
        if group_by is not unset:
            kwargs["group_by"] = group_by
        if indexes is not unset:
            kwargs["indexes"] = indexes
        if storage is not unset:
            kwargs["storage"] = storage
        super().__init__(kwargs)

        self_.data_source = data_source
        self_.query_string = query_string
