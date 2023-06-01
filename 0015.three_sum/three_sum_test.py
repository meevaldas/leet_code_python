import unittest
from three_sum import Solution


class TestThreeSum(unittest.TestCase):
    def test_example_one(self):
        self.assertAlmostEqual(Solution().three_sum([-1, 0, 1, 2, -1, -4]), [[-1, -1, 2], [-1, 0, 1]])

    def test_example_two(self):
        self.assertAlmostEqual(Solution().three_sum([0, 1, 1]), [])

    def test_example_three(self):
        self.assertAlmostEqual(Solution().three_sum([0, 0, 0]), [[0, 0, 0]])
