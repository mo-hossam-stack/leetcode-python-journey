# Problem: 3120. Count the Number of Special Characters I
# LeetCode: https://leetcode.com/problems/count-the-number-of-special-characters-i/
# Difficulty: Easy
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        A=[0, 0]
        for c in word:
            idx=ord(c)
            isLower=idx>=97
            A[isLower]|=(1<<(31&idx))
        return (A[0]&A[1]).bit_count()
