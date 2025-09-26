# Problem: Count Key Changes
# LeetCode: https://leetcode.com/problems/count-key-changes/
# Difficulty: Easy

class Solution:
    def countKeyChanges(self, s: str) -> int:
        s = s.lower()
        ans = 0
        for i in range(len(s) - 1):
            if s[i] != s[i + 1]:
                ans += 1
        return ans