#!/usr/bin/env python3
"""Test for client.py"""

import unittest
from parameterized import parameterized
from utils import requests, get_json
import client
from client import GitHubOrgClient
from unittest.mock import Mock, patch, PropertyMock


class TestGitHubOrgClient(unittest.TestCase):
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
        i = GitHubOrgClient(org)
        self.assertEqual(i.org, True)
        test_payload.assert_called_once()

    def test_public_repos_url(self, org):
        """method to unit-test GitHubOrgClient._public_repos_url"""
        url = f'https://api.github.com/orgs/{org}/repos'
        expected = {'repos_url': url}

        with patch('GithubOrgClient.org',
                   PropertyMock(return_value=expected)):
            i = GitHubOrgClient(org)
            self.assertEqual(i._public_repos_url, url)
