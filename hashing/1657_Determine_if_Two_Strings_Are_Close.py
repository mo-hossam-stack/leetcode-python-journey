# Problem: Determine if Two Strings Are Close
# LeetCode: https://leetcode.com/problems/determine-if-two-strings-are-close/
# Difficulty: Medium

from collections import Counter

class Solution:
    def closeStrings(self, word1, word2):
        if len(word1) != len(word2) or set(word1) != set(word2):
            return False
        count1 = Counter(word1)
        count2 = Counter(word2)
        return sorted(count1.values()) == sorted(count2.values())