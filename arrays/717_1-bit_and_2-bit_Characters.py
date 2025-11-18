# Problem: 1-bit and 2-bit Characters
# LeetCode: https://leetcode.com/problems/1-bit-and-2-bit-characters/
# Difficulty: Easy

class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        n, i = len(bits), 0
        while i < n - 1:
            if bits[i] == 0:
                i += 1
            else:
                i += 2
        return i == n - 1