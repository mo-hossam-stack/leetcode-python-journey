# Problem: 2472. Maximum Number of Non-overlapping Palindrome Substrings
# LeetCode: https://leetcode.com/problems/maximum-number-of-non-overlapping-palindrome-substrings/
# Difficulty: Hard
class Solution:
    def maxPalindromes(self, s, k):
        n = len(s)
        ans = 0
        end = -1

        for i in range(n):
            for l0 in (i - 1, i):
                l, r = l0, i
                while l >= 0 and r < n and s[l] == s[r]:
                    if r - l + 1 >= k and l > end:
                        ans += 1
                        end = r
                        break

                    l -= 1
                    r += 1

        return ans
