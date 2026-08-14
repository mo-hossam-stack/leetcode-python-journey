# Problem: 3090. Maximum Length Substring With Two Occurrences
# LeetCode: https://leetcode.com/problems/maximum-length-substring-with-two-occurrences/
# Difficulty: Easy
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        res = 2
        n = len(s)

        for i in range(n):
            mp = {}
            j = i

            while j < n:
                mp[s[j]] = mp.get(s[j], 0) + 1

                if mp[s[j]] >= 3:
                    break
                j += 1

            res = max(res, j - i)
            i = j

        return res
