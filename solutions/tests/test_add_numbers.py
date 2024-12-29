#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for add_numbers function.

Test categories:
    - Standard cases: typical numbers
    - Edge cases: zero, negative numbers
    - Defensive tests: wrong input types, assertions

Created on 2024-12-06
Author: GitHub Copilot
"""

import unittest
from solutions.add_numbers import add_numbers

class TestAddNumbers(unittest.TestCase):
    """Test suite for the add_numbers function."""

    # Standard test cases
    def test_integers(self):
        """It should return the sum of two integers"""
        self.assertEqual(add_numbers(5, 3), 8)

    def test_floats(self):
        """It should return the sum of two floats"""
        self.assertEqual(add_numbers(4.5, 3.5), 8.0)

    # Edge cases
    def test_zero(self):
        """It should return the sum when one of the numbers is zero"""
        self.assertEqual(add_numbers(0, 5), 5)

    def test_negative_numbers(self):
        """It should return the sum of two negative numbers"""
        self.assertEqual(add_numbers(-2, -3), -5)

    # Defensive tests
    def test_none_input(self):
        """It should raise AssertionError for None input"""
        with self.assertRaises(AssertionError):
            add_numbers(None, 5)

    def test_string_input(self):
        """It should raise AssertionError for string input"""
        with self.assertRaises(AssertionError):
            add_numbers("5", 5)

if __name__ == '__main__':
    unittest.main()
