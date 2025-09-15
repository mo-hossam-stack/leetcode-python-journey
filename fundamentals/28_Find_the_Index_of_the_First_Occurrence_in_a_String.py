# Problem: Find the Index of the First Occurrence in a String
# LeetCode: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
# Difficulty: Easy

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)  # O(n)