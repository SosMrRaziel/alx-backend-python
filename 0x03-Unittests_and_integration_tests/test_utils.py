#!/usr/bin/env python3
""" Test for utils.py """
import unittest
from utils import access_nested_map
from unittest.mock import patch
from utils import get_json


class TestAccessNestedMap(unittest.TestCase):
    """Test access_nested_map function"""
    def test_access_nested_map(self):
        """Tests access_nested_map with the specified inputs."""
        # Test case 1: nested_map={"a": 1}, path=("a",)
        self.assertEqual(access_nested_map({"a": 1}, ("a",)), 1)

        # Test case 2: nested_map={"a": {"b": 2}}, path=("a",)
        self.assertEqual(access_nested_map({"a": {"b": 2}}, ("a",)), {"b": 2})

        # Test case 3: nested_map={"a": {"b": 2}}, path=("a", "b")
        self.assertEqual(access_nested_map({"a": {"b": 2}}, ("a", "b")), 2)

    def test_access_nested_map_exception(self, nested_map, path):
        """Tests KeyError with the specified inputs."""
        with self.assertRaises(KeyError) as e:
            access_nested_map(nested_map, path)
        expected_exception = f"KeyError('{str(path[-1])}')"
        self.assertEqual(repr(e.exception), expected_exception)


class TestGetJson(unittest.TestCase):
    """Test get_json function"""
    @patch("requests.get")
    def test_get_json(self, mock_requests_get):
        # Mock response payload
        test_payload = {"payload": True}

        # Test case 1: test_url="http://example.com"
        mock_requests_get.return_value.json.return_value = test_payload
        result1 = get_json("http://example.com")
        self.assertEqual(result1, test_payload)
        mock_requests_get.assert_called_once_with("http://example.com")

        # Test case 2: test_url="http://holberton.io"
        mock_requests_get.reset_mock()  # Reset mock call count
        test_payload = {"payload": False}
        mock_requests_get.return_value.json.return_value = test_payload
        result2 = get_json("http://holberton.io")
        self.assertEqual(result2, test_payload)
        mock_requests_get.assert_called_once_with("http://holberton.io")


if __name__ == "__main__":
    unittest.main()
