import unittest
from reverse_linked_list import Solution


class TestReverseLinkedList(unittest.TestCase):
    def test_example_one(self):
        self.assertAlmostEqual(Solution().reverse_list([1, 2, 3, 4, 5]), [5, 4, 3, 2, 1])

    def test_example_two(self):
        self.assertAlmostEqual(Solution().reverse_list([1, 2]), [2, 1])

    def test_example_three(self):
        self.assertAlmostEqual(Solution().reverse_list([]), [])
