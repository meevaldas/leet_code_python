import unittest
from insert_interval import Solution


class TestInsertInterval(unittest.TestCase):
    def test_example_one(self):
        self.assertEqual(Solution().insert([[1, 3], [6, 9]], [2, 5]), [[1, 5], [6, 9]])

    def test_example_two(self):
        self.assertEqual(Solution().insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]),
                         [[1, 2], [3, 10], [12, 16]])
