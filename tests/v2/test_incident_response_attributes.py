# coding: utf-8

# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


import sys
import unittest

import datadog_api_client.v2
from datadog_api_client.v2.model.incident_field_attributes import IncidentFieldAttributes
globals()['IncidentFieldAttributes'] = IncidentFieldAttributes
from datadog_api_client.v2.model.incident_response_attributes import IncidentResponseAttributes


class TestIncidentResponseAttributes(unittest.TestCase):
    """IncidentResponseAttributes unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testIncidentResponseAttributes(self):
        """Test IncidentResponseAttributes"""
        # FIXME: construct object with mandatory attributes with example values
        # model = IncidentResponseAttributes()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
