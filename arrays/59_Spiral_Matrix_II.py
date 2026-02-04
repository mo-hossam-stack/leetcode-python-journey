# Problem: 59. Spiral Matrix II
# LeetCode: https://leetcode.com/problems/spiral-matrix-ii/
# Difficulty: Medium

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        def idx_convert_1D_2D(idx):
            return idx // n, idx % n

        # Checking for out of bound condition
        def is_out_of_bound(row, col):
            return row < 0 or row >= n or col < 0 or col >= n

        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        result = [[0] * n for _ in range(n)]

        row =  col = cur_dir_idx = 0 

        for i in range(1, n * n + 1):
            result[row][col] = i
            dx, dy = dirs[cur_dir_idx]
            if (
                is_out_of_bound(row + dx, col + dy)
                or result[row + dx][col + dy] > 0
            ):
                cur_dir_idx = (cur_dir_idx + 1) % 4  # change directions
            dx, dy = dirs[cur_dir_idx]
            row, col = row + dx, col + dy
        return result
