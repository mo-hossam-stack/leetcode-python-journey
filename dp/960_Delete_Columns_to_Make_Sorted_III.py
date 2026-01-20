# Problem: Delete Columns to Make Sorted III
# LeetCode: https://leetcode.com/problems/delete-columns-to-make-sorted-iii/
# Difficulty: Hard

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        cols = len(strs[0])
        rows = len(strs)
        dp = [1] * cols

        for c1 in range(cols - 2, -1, -1):
            for c2 in range(c1 + 1, cols):
                ok = True
                for r in range(rows):
                    if strs[r][c1] > strs[r][c2]:
                        ok = False
                        break
                if ok:
                    dp[c1] = max(dp[c1], 1 + dp[c2])

        return cols - max(dp)
