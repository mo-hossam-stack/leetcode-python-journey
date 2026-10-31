# Problem: 3665. Twisted Mirror Path Count
# LeetCode: https://leetcode.com/problems/twisted-mirror-path-count/
# Difficulty: Medium
class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        mod = 10**9 + 7
        down = [1] + [0] * (len(grid[0]) - 1) 
        for row in grid:
            right = 0
            for j, mirror in enumerate(row):
                if mirror:
                    right, down[j] = down[j], right
                else:
                    right = down[j] = (right + down[j]) % mod
        return down[-1]
