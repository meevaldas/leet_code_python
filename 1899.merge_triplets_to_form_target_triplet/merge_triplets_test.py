import unittest
from merge_triplets import Solution


class TestMergeTriplets(unittest.TestCase):
    def test_example_one(self):
        self.assertAlmostEqual(Solution().merge_triplets([[2, 5, 3], [1, 8, 4], [1, 7, 5]], [2, 7, 5]), True)

    def test_example_two(self):
        self.assertAlmostEqual(Solution().merge_triplets([[3, 4, 5], [4, 5, 6]], [3, 2, 5]), False)

    def test_example_three(self):
        self.assertAlmostEqual(Solution().merge_triplets([[2, 5, 3], [2, 3, 4], [1, 2, 5], [5, 2, 3]], [5, 5, 5]), True)
