import unittest
from unittest import TestCase

from plus_one import Solution


class TestPlusOne(unittest.TestCase):
    def test_example_one(self):
        self.assertAlmostEqual(Solution().plus_one([1, 2, 3]), [1, 2, 4])

    def test_example_two(self):
        self.assertAlmostEqual(Solution().plus_one([4, 3, 2, 1]), [4, 3, 2, 2])
