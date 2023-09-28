import unittest
from maximum_subarray import Solution


class TestMaximumSubarray(unittest.TestCase):
    def test_example_one(self):
        self.assertEqual(Solution().max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)

    def test_example_two(self):
        self.assertEqual(Solution().max_sub_array([1]), 1)
