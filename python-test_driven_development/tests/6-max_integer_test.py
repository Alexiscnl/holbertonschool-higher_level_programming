#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_at_end(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
    def test_reverse_list(self):
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)
    def test_max_at_middle(self):
        self.assertEqual(max_integer([2, 4, 3, 2]), 4)
    def test_list_empty(self):
        self.assertEqual(max_integer([]), None)
    def test_one_el(self):
        self.assertEqual(max_integer([2]), 2)
    def test_max_negativ(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
    def test_negativ_and_positiv(self):
        self.assertEqual(max_integer([0, 2, -5, -1]), 2)
    def test_number_float(self):
        self.assertEqual(max_integer([0.2, 1.8, 0.8, 9.8]), 9.8)
    def test_float_and_int(self):
        self.assertEqual(max_integer([1, 2.5, 8, 0.5]), 8)
    def test_string(self):
        self.assertEqual(max_integer(["hello", "apple", "commit" ]), "hello")
    def test_string_and_int(self):
        with self.assertRaises(TypeError):
            max_integer(["hello", 1, 1.2])
    def test_list_with_none(self):
        with self.assertRaises(TypeError):
            max_integer([None, 1, 2])
