# Problem: 3498. Reverse Degree of a String
# LeetCode: https://leetcode.com/problems/reverse-degree-of-a-string/
# Difficulty: Easy
class Solution:
    def reverseDegree(self, s: str) -> int:
        ans = 0
        for i, c in enumerate(s):
            ans += (26 - (ord(c) - ord('a'))) * (i + 1)
        return ans
