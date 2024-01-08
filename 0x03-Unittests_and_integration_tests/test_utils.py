#!/usr/bin/env python3
from typing import Mapping, Tuple, Union, Any, Type
import unittest
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    '''Test suite for the access_nested_map function.'''

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
            self,
            nested_map: Mapping,
            path: Tuple[int, str],
            expected: Union[Mapping, int]
            ) -> None:
        '''Test access_nested_map with various inputs.'''
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(
            self,
            nested_map: Mapping[Any, Any],
            path: Tuple[str],
            expected: Type[Exception]
            ) -> None:
        '''Test that access_nested_map raises the expected exception.'''
        with self.assertRaises(expected):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    '''Test suite for the get_json function.'''

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')
    def test_get_json(
            self,
            test_url: str,
            test_payload: Mapping,
            mock_get: Mock
            ) -> None:
        '''Test get_json with mocked requests.get.'''
        mock_get.return_value.json.return_value = test_payload

        result = get_json(test_url)

        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    '''Test suite for the memoize decorator.'''

    @patch('utils.TestClass.a_method')
    def test_memoize(self, mock_a_method: Mock) -> None:
        '''Test that memoize decorator works as expected.'''
        test_instance = TestClass()

        # Call a_property twice
        result1 = test_instance.a_property()
        result2 = test_instance.a_property()

        # Check that a_method is only called once
        mock_a_method.assert_called_once()

        # Check that the correct result is returned both times
        self.assertEqual(result1, 42)
        self.assertEqual(result2, 42)


class TestClass:
    '''Test class for memoization.'''

    def a_method(self):
        return 42

    @memoize
    def a_property(self):
        return self.a_method()


if __name__ == '__main__':
    unittest.main()
