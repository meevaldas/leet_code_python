import unittest
from meeting_rooms import Solution


class TestMeetingRooms(unittest.TestCase):
    def test_example_one(self):
        self.assertEqual(Solution().can_attend_meetings([[0, 30], [5, 10], [15, 20]]), False)

    def test_example_two(self):
        self.assertEqual(Solution().can_attend_meetings([[7, 10], [2, 4]]), True)
