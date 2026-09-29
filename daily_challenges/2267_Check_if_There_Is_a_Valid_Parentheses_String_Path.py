# Problem: 2267. Check if There Is a Valid Parentheses String Path
# LeetCode: https://leetcode.com/problems/check-if-there-is-a-valid-parentheses-string-path/
# Difficulty: Hard
class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])

        @lru_cache(None)
        def dfs(row, col, balance):

            if row >= m or col >= n:
                return False

            balance += 1 if grid[row][col] == '(' else -1

            if balance < 0:
                return False

            if row == m - 1 and col == n - 1:
                return balance == 0

            return (
                dfs(row + 1, col, balance) or
                dfs(row, col + 1, balance)
            )

        return dfs(0, 0, 0)
