# Problem: 1758. Minimum Changes To Make Alternating Binary String
# LeetCode: https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/
# Difficulty: Easy

class Solution:
    def minOperations(self, s: str) -> int:
        count, n = 0, len(s)
        for i in range(n):
            count += (ord(s[i]) ^ i) & 1
            
        return min(count, n - count)
