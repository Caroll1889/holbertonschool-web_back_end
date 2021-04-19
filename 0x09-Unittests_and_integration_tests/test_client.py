#!/usr/bin/env python3
"""Test for client.py"""

import unittest
from parameterized import parameterized, param
from utils import requests, get_json
from client import GitHubOrgClient
from unittest.mock import Mock, patch


class TestGitHubOrgClient(unittest.TestCase):
    """Class test for client.py"""

    @parameterized.expand([
        param(org="google", test_payload={"google": True}),
        param(org="abc", test_payload={"abc": True})
    ])
    def test_org(self, org, test_payload):
        """Method test that GitHubOrgClient.org
        returns the correct value.
        """
        with patch('client.get_json', return_value=test_payload) as mock:
            i = GitHubOrgClient(org)
            res = i.org
            self.assertEqual(res, test_payload)
            mock.assert_called_once()
