# Problem: 1888. Minimum Number of Flips to Make the Binary String Alternating
# LeetCode: https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/
# Difficulty: Medium

class Solution:
    def minFlips(self, s):
        n = len(s)
        e, o = (n + 1) // 2, n // 2
        x = s[::2].count('1') - s[1::2].count('1')
        r = min(e - x, o + x)
        if n & 1:
            for c in s:
                x = 2 * (ord(c) & 1) - x
                r = min(r, e - x, o + x)
        return r
