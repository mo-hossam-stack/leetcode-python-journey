# Problem: Count Negative Numbers in a Sorted Matrix
# LeetCode: https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/
# Difficulty: Easy

class Solution:
    def countNegatives(self, grid):
        m, n = len(grid), len(grid[0])
        row, col = m - 1, 0
        count = 0

        while row >= 0 and col < n:
            if grid[row][col] < 0:
                count += (n - col)
                row -= 1
            else:
                col += 1

        return count
