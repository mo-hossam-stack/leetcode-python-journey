# Problem: 1967. Number of Strings That Appear as Substrings in Word
# LeetCode: https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/
# Difficulty: Easy

class Solution:
    def numOfStrings(self, patterns: list[str], word: str) -> int:
        count = 0
        for s in patterns:
            if s in word:
                count += 1
        return count
