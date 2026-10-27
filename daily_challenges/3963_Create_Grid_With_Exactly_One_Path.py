# Problem: 3963. Create Grid With Exactly One Path
# LeetCode: https://leetcode.com/problems/create-grid-with-exactly-one-path/
# Difficulty: Easy
class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        return ["." * n] + ["#" * (n - 1) + "."] * (m - 1)
