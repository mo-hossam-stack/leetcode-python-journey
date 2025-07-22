# Problem: Break a Palindrome
# LeetCode: https://leetcode.com/problems/break-a-palindrome
# Difficulty: Medium

class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        if n == 1:
            return ""

        palindrome_list = list(palindrome)
        for i in range(n // 2):
            if palindrome_list[i] != 'a':
                palindrome_list[i] = 'a'
                return ''.join(palindrome_list)

        palindrome_list[-1] = 'b'
        return ''.join(palindrome_list)