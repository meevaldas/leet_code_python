import unittest
from hand_of_straights import Solution


class TestHandOfStraights(unittest.TestCase):
    def test_example_one(self):
        self.assertEqual(Solution().is_n_straight_hand([1, 2, 3, 6, 2, 3, 4, 7, 8], 3), True)

    def test_example_two(self):
        self.assertEqual(Solution().is_n_straight_hand([1, 2, 3, 4, 5], 4), False)
