# Problem: Delete Columns to Make Sorted II
# LeetCode: https://leetcode.com/problems/delete-columns-to-make-sorted-ii/
# Difficulty: Medium

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        res, n = 0, len(strs)
        m = len(strs[0])
        unsorted = set(range(n - 1)) 

        for j in range(m):
            if any(strs[i][j] > strs[i + 1][j] for i in unsorted):
                res += 1

            else:
                unsorted -= {i for i in unsorted if strs[i][j] < strs[i + 1][j]}

        return res
