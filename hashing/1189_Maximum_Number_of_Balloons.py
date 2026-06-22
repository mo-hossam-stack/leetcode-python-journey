# Problem: 1189. Maximum Number of Balloons
# LeetCode: https://leetcode.com/problems/maximum-number-of-balloons/
# Difficulty: Easy

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        f = Counter(text)
        return min(f["b"], f["a"], f["l"] >> 1, f["o"] >> 1, f["n"])
