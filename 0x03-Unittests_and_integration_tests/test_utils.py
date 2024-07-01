#!/usr/bin/env python3
""" Test for utils.py """
import unittest
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Test access_nested_map function"""
    def test_access_nested_map(self):
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

if __name__ == "__main__":
    unittest.main()
