# Problem: Longest Substring Without Repeating Characters
# LeetCode: https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Difficulty: Medium

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        sett = set()
        max_len = 0
        for r in range(len(s)):
            while s[r] in sett:
                sett.remove(s[l])
                l += 1
            sett.add(s[r])
            max_len = max(max_len, r - l + 1)
        return max_len