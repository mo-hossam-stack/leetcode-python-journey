# Problem: Reverse Linked List
# LeetCode: https://leetcode.com/problems/reverse-linked-list/
# Difficulty: Easy

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr != None:
            next_pointer = curr.next
            curr.next = prev
            prev = curr
            curr = next_pointer
        return prev