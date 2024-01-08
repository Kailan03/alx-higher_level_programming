#!/usr/bin/python3
import unittest
from max_integer import max_integer

class TestMaxInteger(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(max_integer([1, 3, 5, 7, 9]), 9)
        self.assertEqual(max_integer([15, 2, 10, 8]), 15)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-5, -2, -8, -1]), -1)
        self.assertEqual(max_integer([-10, -15, -3]), -3)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([1, -3, 5, -7, 9]), 9)
        self.assertEqual(max_integer([-15, 2, -10, 8]), 8)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_single_element_list(self):
        self.assertEqual(max_integer([42]), 42)

    def test_duplicate_numbers(self):
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

    def test_float_numbers(self):
        self.assertEqual(max_integer([1.5, 2.3, 0.8, 1.2]), 2.3)

    def test_mixed_data_types(self):
        with self.assertRaises(TypeError):
            max_integer([1, 'two', 3, 4])

if __name__ == '__main__':
    unittest.main()
