# Problem: Maximum Matrix Sum
# LeetCode: https://leetcode.com/problems/maximum-matrix-sum/
# Difficulty: Medium

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total = 0
        neg_count = 0
        min_abs = float('inf')

        for row in matrix:
            for x in row:
                total += abs(x)
                if x < 0:
                    neg_count += 1
                min_abs = min(min_abs, abs(x))

        if neg_count % 2 == 0:
            return total
        else:
            return total - 2 * min_abs
            https://leetcode.com/problems/maximum-matrix-sum/
           1975. Maximum Matrix Sum
