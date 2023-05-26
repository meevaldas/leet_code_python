import unittest# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from product_of_array_except_self import Solution


class TestProductOfArrayExceptSelf(unittest.TestCase):
    def test_product_of_array_except_self_example_one(self):
        self.assertAlmostEqual(Solution().product_except_self([1, 2, 3, 4]), [24, 12, 8, 6])

    def test_product__of_array_except_self_example_two(self):
        self.assertAlmostEqual(Solution().product_except_self([-1, 1, 0, -3, 3]), [0, 0, 9, 0, 0])
