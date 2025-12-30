# Problem: Magic Squares In Grid
# LeetCode: https://leetcode.com/problems/magic-squares-in-grid/
# Difficulty: Medium

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        res = 0

        def valid(i, j):
            nums = set()
            for r in range(i - 2, i + 1):
                for c in range(j - 2, j + 1):
                    if grid[r][c] in nums:
                        return False
                    nums.add(grid[r][c])

            sd1 = grid[i-2][j-2] + grid[i-1][j-1] + grid[i][j]
            sd2 = grid[i-2][j] + grid[i-1][j-1] + grid[i][j-2]
            if sd1 != sd2:
                return False

            for r in range(i - 2, i + 1):
                if grid[r][j-2] + grid[r][j-1] + grid[r][j] != sd1:
                    return False

            for c in range(j - 2, j + 1):
                if grid[i-2][c] + grid[i-1][c] + grid[i][c] != sd1:
                    return False

            return nums == set(range(1, 10))

        for i in range(2, n):
            for j in range(2, m):
                if valid(i, j):
                    res += 1
        return res
