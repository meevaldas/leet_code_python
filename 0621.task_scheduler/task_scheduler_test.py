import unittest
from task_scheduler import Solution


class TestTaskScheduler(unittest.TestCase):
    def test_example_one(self):
        self.assertEqual(Solution().least_interval(["A", "A", "A", "B", "B", "B"], 2), 8)

    def test_example_two(self):
        self.assertEqual(Solution().least_interval(["A", "A", "A", "B", "B", "B"], 0), 6)
