# Problem: 52. N-Queens II
# LeetCode: https://leetcode.com/problems/n-queens-ii/
# Difficulty: Hard

class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(row, cols, diag1, diag2):
            if row == n:
                return 1
            count = 0
            available = ((1 << n) - 1) & ~(cols | diag1 | diag2)
            while available:
                bit = available & -available
                available -= bit
                count += backtrack(row + 1, cols | bit, (diag1 | bit) << 1, (diag2 | bit) >> 1)
            return count
        return backtrack(0, 0, 0, 0)
