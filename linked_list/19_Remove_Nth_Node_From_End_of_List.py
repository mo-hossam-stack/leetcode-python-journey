# Problem: Remove Nth Node From End of List
# LeetCode: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Difficulty: Medium

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        behind = ahead = dummy

        for _ in range(n+1):
            ahead = ahead.next 

        while ahead:
            behind = behind.next
            ahead = ahead.next

        behind.next = behind.next.next
        return dummy.
