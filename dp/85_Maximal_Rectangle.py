# Problem: Maximal Rectangle
# LeetCode: https://leetcode.com/problems/maximal-rectangle/
# Difficulty: Hard

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        M = len(matrix)
        N = len(matrix[0])

        for i in range(M):
            for j in range(N):
                matrix[i][j] = int(matrix[i][j])

        for i in range(M):
            for j in range(1, N):
                if matrix[i][j] == 1:
                    matrix[i][j] += matrix[i][j - 1]

        ans = 0

        for j in range(N):
            for i in range(M):
                width = matrix[i][j]
                if width == 0:
                    continue

                curr_width = width
                k = i
                while k < M and matrix[k][j] > 0:
                    curr_width = min(curr_width, matrix[k][j])
                    height = k - i + 1
                    ans = max(ans, curr_width * height)
                    k += 1

                curr_width = width
                k = i
                while k >= 0 and matrix[k][j] > 0:
                    curr_width = min(curr_width, matrix[k][j])
                    height = i - k + 1
                    ans = max(ans, curr_width * height)
                    k -= 1

        return ans
