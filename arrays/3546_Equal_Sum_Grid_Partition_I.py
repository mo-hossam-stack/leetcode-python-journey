# Problem: 3546. Equal Sum Grid Partition I
# LeetCode: https://leetcode.com/problems/equal-sum-grid-partition-i/
# Difficulty: Medium

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        total = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(1, n):
            grid[0][i] += grid[0][i-1]
        for i in range(1, m):
            grid[i][0] += grid[i-1][0]
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += grid[i-1][j] + grid[i][j-1] - grid[i-1][j-1]
        
        total = grid[m-1][n-1]
        if total & 1:
            return False
            
        target = total >> 1
        
        idx_v = bisect_left(grid[-1], target)
        if idx_v < n and grid[-1][idx_v] == target:
            return True
            
        last_col = [row[-1] for row in grid]
        idx_h = bisect_left(last_col, target)
        if idx_h < m and last_col[idx_h] == target:
            return True
            
        return False
