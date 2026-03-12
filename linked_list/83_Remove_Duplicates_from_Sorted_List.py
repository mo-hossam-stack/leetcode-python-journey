# Problem: 83. Remove Duplicates from Sorted List
# LeetCode: https://leetcode.com/problems/remove-duplicates-from-sorted-list/
# Difficulty: Easy

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr and curr.next:
            if curr.val == curr.next.val:
                # Link current node to the one after the duplicate
                curr.next = curr.next.next
            else:
                # Move forward only if no duplicate was found
                curr = curr.next
        return head
