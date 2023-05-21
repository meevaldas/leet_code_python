import unittest
from count_the_no_of_bad_pairs import Solution


class TestCountBadPairs(unittest.TestCase):
    def test_count_bad_pairs_example_one(self):
        self.assertAlmostEqual(Solution().count_bad_pairs([4, 1, 3, 3]), 5)

    def test_count_bad_pairs_example_two(self):
        self.assertAlmostEqual(Solution().count_bad_pairs([1, 2, 3, 4, 5]), 0)
