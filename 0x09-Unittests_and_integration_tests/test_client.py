#!/usr/bin/env python3
"""Test for client.py"""

import unittest
from parameterized import parameterized, param
from utils import requests, get_json
import client
from client import GithubOrgClient
from unittest.mock import Mock, patch, PropertyMock


class TestGithubOrgClient(unittest.TestCase):
    """Class test for client.py"""

    @parameterized.expand([
        param(org="google", test_payload={"payload": True}),
        param(org="abc", test_payload={"payload": False})
    ])
    def test_org(self, org, test_payload):
        """Method test that GitHubOrgClient.org
        returns the correct value.
        """
        with patch('client.get_json', return_value=test_payload) as mock:
            i = GithubOrgClient(org_name=org)
            res = i.org
            self.assertEqual(res, test_payload)
            mock.assert_called_once()

    def test_public_repos_url(self, org):
        """Method to unit-test GitHubOrgClient._public_repos_url"""
        url = f'https://api.github.com/orgs/{org}/repos'
        expected = {'repos_url': url}

        with patch('GithubOrgClient.org',
                   PropertyMock(return_value=expected)):
            i = GithubOrgClient(org)
            self.assertEqual(i._public_repos_url, url)

    @patch('client.get_json')
    def test_public_repos(self, test_payload):
        """Method to unit-test GitHubOrgClient.public_repos"""
        return_value = [{'name': 'google'}, {'name': 'abc'}]
        test_payload.return_value = return_value

        with patch('GithubOrgClient._public_repos_url',
                   PropertyMock(return_value=return_value)) as mock:
            i = GithubOrgClient('test')
            self.assertEqual(i.public_repos(), ['google', 'abc'])
            test_payload.assert_called_once()
            mock.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, rep, key, license):
        """Method to unit-test GithubOrgClient.has_license"""
        self.assertEqual(GithubOrgClient.has_license(rep, key), license)
