# Problem: Palindrome Number
# LeetCode: https://leetcode.com/problems/palindrome-number/
# Difficulty: Easy

class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        return s==s[::-1]