
import unittest
from src.selection_sort import selection_sort

class TestSelectionSort(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(selection_sort([]), [])

    def test_single_element(self):
        self.assertEqual(selection_sort([5]), [5])

    def test_sorted_list(self):
        self.assertEqual(selection_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_unsorted_list(self):
        self.assertEqual(selection_sort([4, 2, 5, 1, 3]), [1, 2, 3, 4, 5])

    def test_duplicates(self):
        self.assertEqual(selection_sort([4, 4, 3, 2, 2]), [2, 2, 3, 4, 4])

    def test_negative_numbers(self):
        self.assertEqual(selection_sort([3, -1, 2, -5, 0]), [-5, -1, 0, 2, 3])

if __name__ == '__main__':
    unittest.main()
