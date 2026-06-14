# Problem: 2130. Maximum Twin Sum of a Linked List
# LeetCode: https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/
# Difficulty: Medium

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = fast = head
        prev = None

        while fast and fast.next:
            fast = fast.next.next
            slow.next, prev, slow = prev, slow, slow.next

        res = 0
        while slow:
            res = max(res, prev.val + slow.val)
            prev, slow = prev.next, slow.next

        return res
