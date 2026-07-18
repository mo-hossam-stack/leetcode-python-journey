# Problem: 3992. Rearrange String to Avoid Character Pair
# LeetCode: https://leetcode.com/problems/rearrange-string-to-avoid-character-pair/
# Difficulty: Medium

class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        ys = [char for char in s if char == y]
        xs = [char for char in s if char == x]
        others = [char for char in s if char != x and char != y]
        return "".join(ys + others + xs)
