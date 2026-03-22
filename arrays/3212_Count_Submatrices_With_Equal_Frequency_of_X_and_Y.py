# Problem: 3212. Count Submatrices With Equal Frequency of X and Y
# LeetCode: https://leetcode.com/problems/count-submatrices-with-equal-frequency-of-x-and-y/
# Difficulty: Medium

class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        ans = 0
        sum = [[[0, 0] for _ in range(m + 1)] for _ in range(n + 1)]

        for i in range(n):
            for j in range(m):
                if grid[i][j] == "X":
                    sum[i + 1][j + 1][0] = (
                        sum[i + 1][j][0] + sum[i][j + 1][0] - sum[i][j][0] + 1
                    )
                    sum[i + 1][j + 1][1] = 1
                elif grid[i][j] == "Y":
                    sum[i + 1][j + 1][0] = (
                        sum[i + 1][j][0] + sum[i][j + 1][0] - sum[i][j][0] - 1
                    )
                    sum[i + 1][j + 1][1] = sum[i + 1][j][1] | sum[i][j + 1][1]
                else:
                    sum[i + 1][j + 1][0] = (
                        sum[i + 1][j][0] + sum[i][j + 1][0] - sum[i][j][0]
                    )
                    sum[i + 1][j + 1][1] = sum[i + 1][j][1] | sum[i][j + 1][1]
                if sum[i + 1][j + 1][0] == 0 and sum[i + 1][j + 1][1] == 1:
                    ans += 1

        return ans
