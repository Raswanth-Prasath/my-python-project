"""Tests for the core module."""

import unittest
from my_package.core import hello_world, add


class TestCore(unittest.TestCase):
    """Test cases for core functions."""

    def test_hello_world(self):
        """Test the hello_world function."""
        self.assertEqual(hello_world(), "Hello, World!")

    def test_add(self):
        """Test the add function."""
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)


if __name__ == "__main__":
    unittest.main()