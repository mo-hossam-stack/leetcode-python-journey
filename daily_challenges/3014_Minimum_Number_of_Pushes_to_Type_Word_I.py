# Problem: 3014. Minimum Number of Pushes to Type Word I
# LeetCode: https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-i/
# Difficulty: Easy

class Solution:
    def minimumPushes(self, word: str) -> int:

        pushes = 0

        for i in range(len(word)):

            pushes += (i // 8) + 1

        return pushes
