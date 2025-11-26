# Problem: Minimum Path Sum
# LeetCode: https://leetcode.com/problems/minimum-path-sum/
# Difficulty: Medium

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
 
        mem = {}
        def search(x, y):
            if x >= m or y >= n:
                return float('inf')
            if x == m-1 and y == n-1:
                return grid[x][y]
            if (x,y) in mem:
                return mem[(x,y)]
            D = search(x+1, y)
            R = search(x, y+1)
            ans = min(D,R) + grid[x][y]
            mem[(x,y)] = ans
            return ans
        return search(0,0)
