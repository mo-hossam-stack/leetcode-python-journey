# Problem: Swap Nodes in Pairs
# LeetCode: https://leetcode.com/problems/swap-nodes-in-pairs/
# Difficulty: Medium

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev , curr = dummy, head

        while curr and curr.next:
            nxtPair = curr.next.next
            sec = curr.next

            sec.next = curr
            curr.next = nxtPair
            prev.next = sec

            prev = curr
            curr = nxtPair

        return dummy.next
