# Problem: 160. Intersection of Two Linked Lists
# LeetCode: https://leetcode.com/problems/intersection-of-two-linked-lists/
# Difficulty: Easy

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lista = headA
        listb = headB

        while lista != listb:
            lista = lista.next if lista else headB
            listb = listb.next if listb else headA
        
        return listb
