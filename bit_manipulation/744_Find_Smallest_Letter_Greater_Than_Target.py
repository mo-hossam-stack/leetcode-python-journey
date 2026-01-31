# Problem: Find Smallest Letter Greater Than Target
# LeetCode: https://leetcode.com/problems/find-smallest-letter-greater-than-target/
# Difficulty: Easy

class Solution:
    def nextGreatestLetter(self, L: List[str], target: str) -> str:
        return L[i] if (i:=bisect_right(L, target))<len(L) else L[0]
