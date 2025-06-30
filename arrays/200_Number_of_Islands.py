# Problem: Number of Islands
# LeetCode: https://leetcode.com/problems/number-of-islands/
# Difficulty: med

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        count = 0

        def bfs(r, c):
            queue = [(r, c)]
            visited.add((r, c))

            while queue:
                row, col = queue.pop(0)

                for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                    new_row = row + dr
                    new_col = col + dc

                    if (
                        0 <= new_row < rows and
                        0 <= new_col < cols and
                        grid[new_row][new_col] == "1" and
                        (new_row, new_col) not in visited
                    ):
                        queue.append((new_row, new_col))
                        visited.add((new_row, new_col))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    count += 1

        return count
