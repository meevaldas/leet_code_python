"""
Given the head of a singly linked list, reverse the list, and return the reversed list.
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None

        while head:
            temp = head
            head = head.next
            temp.next = prev
            prev = temp
        return prev

