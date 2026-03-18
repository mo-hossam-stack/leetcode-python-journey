# Problem: 3070. Count Submatrices with Top-Left Element and Sum Less Than k
# LeetCode: https://leetcode.com/problems/count-submatrices-with-top-left-element-and-sum-less-than-k/
# Difficulty: Medium

class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        n, m = len(grid), len(grid[0])
        cols = [0] * m
        res = 0

        for i in range(n):
            row_sum = 0
            for j in range(m):
                cols[j] += grid[i][j]
                row_sum += cols[j]
                if row_sum <= k:
                    res += 1

        return res
