# Problem: 1784. Check if Binary String Has at Most One Segment of Ones
# LeetCode: https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/
# Difficulty: Easy

class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        return "01" not in s
