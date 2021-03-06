"""
Unit tests for InfluxDBSettings class
"""

import unittest

from ..perfmonitoring import InfluxDBSettings


class InfluxDBSettingsTest(unittest.TestCase):
    """
    Test InfluxDBSettings
    """
    def test_is_dev(self):
        """
        Test is_dev property
        """
        cases = [
            {
                "environ": {},
                "expected_is_dev": True
            },
            {
                "environ": {
                    'WIKIA_ENVIRONMENT': ''
                },
                "expected_is_dev": False
            },
            {
                "environ": {
                    'WIKIA_ENVIRONMENT': 'dev'
                },
                "expected_is_dev": True
            },
            {
                "environ": {
                    'WIKIA_ENVIRONMENT': 'prod'
                },
                "expected_is_dev": False
            },
            {
                "environ": {
                    'WIKIA_ENVIRONMENT': 'foo'
                },
                "expected_is_dev": False
            },
        ]

        for case in cases:
            self.check_is_dev(**case)

    @staticmethod
    def check_is_dev(environ, expected_is_dev):
        assert InfluxDBSettings(environ).is_dev is expected_is_dev
