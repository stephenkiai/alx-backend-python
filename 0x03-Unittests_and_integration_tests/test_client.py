import unittest
from unittest.mock import patch
from client import GithubOrgClient
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    '''Test suite for the GithubOrgClient class.'''

    @parameterized.expand([
        ('google',),
        ('abc',),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        '''Test that GithubOrgClient.org returns the correct value.'''
        test_instance = GithubOrgClient(org_name)

        # Set up the mock to return a specific value
        mock_get_json.return_value = {'organization': org_name}

        # Call the method under test
        result = test_instance.org

        # Check that get_json is called once with the expected argument
        mock_get_json.assert_called_once_with(
            f'https://api.github.com/orgs/{org_name}')

        # Check that the correct result is returned
        self.assertEqual(result, {'organization': org_name})

    @parameterized.expand([
        ('google', 10),
        ('abc', 5),
    ])
    @patch('client.get_json')
    def test_public_repos(self, org_name, expected_repos, mock_get_json):
        '''Test GithubOrgClient.public_repos.'''
        test_instance = GithubOrgClient(org_name)

        # Set up the mock to return a list of public repos
        mock_get_json.return_value = [{'name': f'repo{i}'}
                                      for i in range(expected_repos)]

        # Call the method under test
        result = test_instance.public_repos()

        # Check that get_json is called once with the expected argument
        mock_get_json.assert_called_once_with(
            f'https://api.github.com/orgs/{org_name}/repos')

        # Check that the correct number of public repos is returned
        self.assertEqual(result, expected_repos)

    @parameterized.expand([
        ('google', 3),
        ('abc', 2),
    ])
    @patch('client.get_json')
    def test_public_repos_with_license(self,
                                       org_name,
                                       expected_repos,
                                       mock_get_json):
        '''Test GithubOrgClient.public_repos with license argument.'''
        test_instance = GithubOrgClient(org_name)

        # Set up the mock to return list of public repos with specified license
        mock_get_json.return_value = [{
            'name': f'repo{i}', 'license': {'spdx_id': 'apache-2.0'}}
            for i in range(expected_repos)]

        # Call the method under test with license="apache-2.0"
        result = test_instance.public_repos(license="apache-2.0")

        # Check that get_json is called once with the expected argument
        mock_get_json.assert_called_once_with(
            f'https://api.github.com/orgs/{org_name}/repos',
            params={'license': 'apache-2.0'})

        # Check correct number of public repos with specfied licnse is returned
        self.assertEqual(result, expected_repos)


if __name__ == '__main__':
    unittest.main()
