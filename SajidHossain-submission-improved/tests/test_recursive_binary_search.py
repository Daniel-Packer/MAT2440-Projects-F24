
import unittest
from src.recursive_binary_search import recursive_binary_search

class TestRecursiveBinarySearch(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(recursive_binary_search([], 5), -1)

    def test_single_element_found(self):
        self.assertEqual(recursive_binary_search([5], 5), 0)

    def test_single_element_not_found(self):
        self.assertEqual(recursive_binary_search([5], 3), -1)

    def test_element_found(self):
        self.assertEqual(recursive_binary_search([1, 2, 3, 4, 5], 3), 2)

    def test_element_not_found(self):
        self.assertEqual(recursive_binary_search([1, 2, 3, 4, 5], 6), -1)

    def test_negative_numbers(self):
        self.assertEqual(recursive_binary_search([-5, -3, 0, 2, 4], -3), 1)

if __name__ == '__main__':
    unittest.main()
