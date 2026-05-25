# Problem: 148. Sort List
# LeetCode: https://leetcode.com/problems/sort-list/
# Difficulty: Medium
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []

        while head:
            arr.append(head.val)
            head = head.next

        arr.sort()

        dummy = ListNode(0)
        cur = dummy

        for num in arr:
            cur.next = ListNode(num)
            cur = cur.next

        return dummy.next
