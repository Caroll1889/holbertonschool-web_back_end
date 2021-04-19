#!/usr/bin/env python3
"""Test for client.py"""

import unittest
from parameterized import parameterized
from utils import requests, get_json
import client
from client import GitHubOrgClient
from unittest.mock import Mock, patch


class TestGithubOrgClient(unittest.TestCase):
    """Class test for client.py"""

    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch('client.get_json')
    def test_org(self, org, test_payload):
        """Method test that GitHubOrgClient.org
        returns the correct value.
        """
        test_payload.return_value = True
        i = client.GitHubOrgClient(org)
        self.assertEqual(i.org, True)
        test_payload.assert_called_once()
