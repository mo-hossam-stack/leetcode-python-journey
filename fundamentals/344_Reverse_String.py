# Problem:  Reverse String
# LeetCode: https://leetcode.com/problems/reverse-string/
# Difficulty: Easy

class Solution:
    def reverseString(self, s: List[str]) -> None:
         s[:] = s[::-1]
        