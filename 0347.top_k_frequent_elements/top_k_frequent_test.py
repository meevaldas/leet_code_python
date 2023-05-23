import unittest
from top_k_frequent_elements import Solution


class TestKFrequentElements(unittest.TestCase):
    def test_k_frequent_example_one(self):
        self.assertAlmostEqual(Solution().top_k_frequent([1, 1, 1, 2, 2, 3], 2), [1, 2])

    def test_k_frequent_example_two(self):
        self.assertAlmostEqual(Solution().top_k_frequent([1], 1), [1])
