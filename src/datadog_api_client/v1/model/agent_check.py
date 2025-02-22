# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
    date,
    datetime,
    none_type,
)


class AgentCheck(ModelSimple):
    """
    Array of strings.


    :type value: [bool, date, datetime, dict, float, int, list, str, none_type]
    """

    @cached_property
    def openapi_types(_):
        return {
            "value": ([bool, date, datetime, dict, float, int, list, str, none_type],),
        }
