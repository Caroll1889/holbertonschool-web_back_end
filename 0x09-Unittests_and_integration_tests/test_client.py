#!/usr/bin/env python3
"""Test for client.py"""

import unittest
from parameterized import parameterized
from utils import requests, get_json
from client import GitHubOrgClient
from unittest.mock import Mock, patch


class TestGitHubOrgClient(unittest.TestCase):
    """Class test for client.py"""

    @parameterized.expand([
        ("google", {"google": True}),
        ("abc", {"abc": True})
    ])
    @patch('client.get_json')
    def test_org(self, org, test_payload, expected):
        """Method test that GitHubOrgClient.org
        returns the correct value.
        """
        test_payload.return_value = expected
        i = GitHubOrgClient(org)
        self.assertEqual(i.org, expected)
        test_payload.assert_called_once()

    def test_public_repos_url(self):
        """Function that test client._public_repos_url"""
        pass
