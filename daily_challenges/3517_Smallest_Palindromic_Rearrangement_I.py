# Problem: 3517. Smallest Palindromic Rearrangement I
# LeetCode: https://leetcode.com/problems/smallest-palindromic-rearrangement-i/
# Difficulty: Medium

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        freq = [0] * 26

        for c in s:
            freq[ord(c) - ord('a')] += 1

        n = len(s)
        ans = [''] * n

        left, right = 0, n - 1

        for i in range(26):
            while freq[i] >= 2:
                ans[left] = chr(ord('a') + i)
                ans[right] = chr(ord('a') + i)
                left += 1
                right -= 1
                freq[i] -= 2

            if freq[i] == 1:
                ans[n // 2] = chr(ord('a') + i)

        return ''.join(ans)
