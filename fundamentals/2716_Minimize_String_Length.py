# Problem: Minimize String Length
# LeetCode: https://leetcode.com/problems/minimize-string-length/
# Difficulty: Easy

class Solution:
    def minimizedStringLength(self, s):
        return len(set(s))