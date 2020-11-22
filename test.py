from structures import Array
from sort import *
import numpy as np
import unittest
import utils


class TestUtils(unittest.TestCase):
    def test_generate_ordered_asc(self):
        expected = Array(np.array([1, 2, 3, 4, 5]))
        actual = utils.generate_ordered_array(5)
        self.assertTrue(np.array_equal(expected, actual), "Expected generated array to be sorted")

    def test_generate_ordered_desc(self):
        expected = Array(np.array([5, 4, 3, 2, 1]))
        actual = utils.generate_ordered_array(5, order='DESC')
        self.assertTrue(np.array_equal(expected, actual), "Expected generated array to be sorted")

    def test_generate_shuffled(self):
        not_expected = Array(np.array([1, 2, 3, 4, 5]))
        actual = utils.generate_shuffled_array(5)
        self.assertFalse(np.array_equal(not_expected, actual), "🍒🍒🍒 jackpot! Chance of that was ~0,008")


class TestSorts(unittest.TestCase):
    def test_bubble(self):
        expected = Array(np.array([1, 2, 3, 4, 5]))
        actual = bubble.sorted(Array(np.array([5, 4, 3, 2, 1])))
        self.assertTrue(np.array_equal(expected, actual), "Expected array to be sorted")

    def test_cocktail_shaker(self):
        expected = Array(np.array([1, 2, 3, 4, 5]))
        actual = cocktail_shaker.sorted(Array(np.array([5, 4, 3, 2, 1])))
        self.assertTrue(np.array_equal(expected, actual), "Expected array to be sorted")

    def test_insertion(self):
        expected = Array(np.array([1, 2, 3, 4, 5]))
        actual = insertion.sorted(Array(np.array([5, 4, 3, 2, 1])))
        self.assertTrue(np.array_equal(expected, actual), "Expected array to be sorted")

    def test_merge(self):
        expected = Array(np.array([1, 2, 3, 4, 5]))
        actual = merge.sorted(Array(np.array([5, 4, 3, 2, 1])))
        self.assertTrue(np.array_equal(expected, actual), "Expected array to be sorted")

    def test_quick(self):
        expected = Array(np.array([1, 2, 3, 4, 5]))
        actual = quick.sorted(Array(np.array([5, 4, 3, 2, 1])))
        self.assertTrue(np.array_equal(expected, actual), "Expected array to be sorted")

    def test_counting(self):
        expected = Array(np.array([1, 2, 3, 4, 5]))
        actual = counting.sorted(Array(np.array([5, 4, 3, 2, 1])))
        self.assertTrue(np.array_equal(expected, actual), "Expected array to be sorted")


if __name__ == 'main':
    unittest.main()
