# Problem: 1260. Shift 2D Grid
# LeetCode: https://leetcode.com/problems/shift-2d-grid/
# Difficulty: Easy

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        if not k: 
            return grid
        r, c = len(grid), len(grid[0])
        n = r * c
        k %= n
        if not k: 
            return grid

        def shift(i, j):
            while i < j:
                grid[i // c][i % c], grid[j // c][j % c] = grid[j // c][j % c], grid[i // c][i % c]
                i += 1
                j -= 1

        shift(0, n - 1)
        shift(0, k - 1)
        shift(k, n - 1)
        
        return grid
