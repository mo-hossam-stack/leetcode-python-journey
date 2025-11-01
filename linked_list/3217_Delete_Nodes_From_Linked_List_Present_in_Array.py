# Problem: Delete Nodes From Linked List Present in Array
# LeetCode: https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/
# Difficulty: Medium

class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        s = set(nums)
        while head and head.val in s:
            head = head.next
        if not head:
            return None
        curr = head
        while curr.next:
            if curr.next.val in s:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head
