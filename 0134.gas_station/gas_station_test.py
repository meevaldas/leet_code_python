import unittest
from gas_station import Solution


class TestGasStation(unittest.TestCase):
    def test_example_one(self):
        self.assertEqual(Solution().can_complete_circuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]), 3)

    def test_example_two(self):
        self.assertEqual(Solution().can_complete_circuit([2, 3, 4], [3, 4, 3]), -1)
