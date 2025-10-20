# Problem: Swim in Rising Water
# LeetCode: https://leetcode.com/problems/swim-in-rising-water/
# Difficulty: Hard

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        h = [[grid[0][0], 0, 0]]
        seen = set((0, 0))
        while h:
            t, i, j = heapq.heappop(h)
            if i == n - 1 and j == n - 1:
                return t
            for ni, nj in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                if ni < 0 or nj < 0 or ni >= n or nj >= n or (ni, nj) in seen:
                    continue
                seen.add((ni, nj))
                heapq.heappush(h, (max(t, grid[ni][nj]), ni, nj))