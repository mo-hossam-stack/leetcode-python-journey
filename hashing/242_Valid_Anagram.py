# Problem: Valid Anagram
# LeetCode: https://leetcode.com/problems/valid-anagram/
# Difficulty: easy


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter_s = Counter(s)
        counter_t = Counter(t)
        return counter_s == counter_t
