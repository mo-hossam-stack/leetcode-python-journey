# Problem: Reverse Linked List II
# LeetCode: https://leetcode.com/problems/reverse-linked-list-ii/
# Difficulty: Medium

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy_head = ListNode(-1, head)
        left_prev, curr_node = dummy_head, head

        for i in range(left - 1):
            left_prev, curr_node = curr_node, curr_node.next

        prev = None
        for i in range(right - left + 1):
            next_pointer = curr_node.next
            curr_node.next = prev
            prev, curr_node = curr_node, next_pointer

        left_prev.next.next = curr_node
        left_prev.next = prev
        return dummy_head.next
