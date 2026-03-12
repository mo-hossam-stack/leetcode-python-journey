# Problem: 82. Remove Duplicates from Sorted List II
# LeetCode: https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
# Difficulty: Medium

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        cur = head

        while cur and cur.next:
            if cur.val == cur.next.val:
                while cur.next and cur.val == cur.next.val:
                    cur = cur.next
                # Skip all nodes with the duplicate value
                prev.next = cur.next  
            else:
                # Move prev only if current node is unique
                prev = prev.next  
            cur = cur.next

        return dummy.next
