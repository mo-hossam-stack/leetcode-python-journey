# Problem: Length of Last Word
# LeetCode: https://leetcode.com/problems/length-of-last-word/
# Difficulty: Easy

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(' ')[-1])