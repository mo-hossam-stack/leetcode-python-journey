# Problem: 2914. Minimum Number of Changes to Make Binary String Beautiful
# LeetCode: https://leetcode.com/problems/minimum-number-of-changes-to-make-binary-string-beautiful/
# Difficulty: Medium
class Solution:
    def minChanges(self, s: str) -> int:
        ans = 0
        for i in range(0, len(s), 2):
            if s[i] != s[i + 1]:
                ans += 1
        return ans
