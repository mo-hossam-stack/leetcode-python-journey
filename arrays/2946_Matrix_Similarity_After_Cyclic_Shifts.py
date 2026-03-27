# Problem: 2946. Matrix Similarity After Cyclic Shifts
# LeetCode: https://leetcode.com/problems/matrix-similarity-after-cyclic-shifts/
# Difficulty: Easy

class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m, n = len(mat), len(mat[0])
        k %= n

        for i in range(m):
            for j in range(n):
                if mat[i][j] != mat[i][(j + k) % n]:
                    return False
        return True
