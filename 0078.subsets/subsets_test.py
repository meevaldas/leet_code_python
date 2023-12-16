import unittest
from subsets import Solution


class TestSubsets(unittest.TestCase):
    def test_example_one(self):
        self.assertCountEqual(Solution().subsets([1, 2, 3]), [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]])

    def test_example_two(self):
        self.assertCountEqual(Solution().subsets([0]), [[], [0]])
