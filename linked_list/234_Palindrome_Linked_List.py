# Problem: Palindrome Linked List
# LeetCode: https://leetcode.com/problems/palindrome-linked-list/
# Difficulty: Easy

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        # Find middle (slow) and end (fast)
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # Reverse second half
        prev = None
        while slow:
            n_pointer = slow.next
            slow.next = prev
            prev = slow
            slow = n_pointer
        # Compare first and second half
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True
