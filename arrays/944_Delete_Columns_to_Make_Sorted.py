# Problem: Delete Columns to Make Sorted
# LeetCode: https://leetcode.com/problems/delete-columns-to-make-sorted/
# Difficulty: Easy

class Solution:

    def minDeletionSize(self, strs: List[str]) -> int:

        res = 0
        rows = len(strs)
        cols = len(strs[0])

        for c in range(cols):
            for r in range(1, rows):
                if strs[r][c] < strs[r-1][c]:
                    res += 1
                    break

        return res
