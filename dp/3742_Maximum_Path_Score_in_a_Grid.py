# Problem: 3742. Maximum Path Score in a Grid
# LeetCode: https://leetcode.com/problems/maximum-path-score-in-a-grid/
# Difficulty: Medium
class Solution(object):
    def maxPathScore(self, grid, k):
        m, n = len(grid), len(grid[0])
        memo = [[[-1 for _ in range(k + 1)] for _ in range(n)] for _ in range(m)]

        def solve(i, j, cost):
            if i >= m or j >= n:
                return float("-inf")

            current_cost = cost + (1 if grid[i][j] > 0 else 0)
            
            if current_cost > k:
                return float("-inf")

            if i == m - 1 and j == n - 1:
                return grid[i][j]

            if memo[i][j][current_cost] != -1:
                return memo[i][j][current_cost]

            res_right = solve(i, j + 1, current_cost)
            res_down = solve(i + 1, j, current_cost)

            best_path = max(res_right, res_down)

            if best_path == float("-inf"):
                ans = float("-inf")
            else:
                ans = grid[i][j] + best_path

            memo[i][j][current_cost] = ans
            return ans

        final_ans = solve(0, 0, 0)
        return final_ans if final_ans != float("-inf") else -1
