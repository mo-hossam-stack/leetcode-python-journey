# Problem: Trapping Rain Water II
# LeetCode: https://leetcode.com/problems/trapping-rain-water-ii/
# Difficulty: Hard

class Solution:
    def trapRainWater(self, A: List[List[int]]) -> int:
        m, n = len(A), len(A[0])
        heap = []
        border = set()

        for i in range(m):
            for j in range(n):
                if i in [0, m - 1] or j in [0, n - 1]:
                    border.add((i, j))
                    heappush(heap, (A[i][j], i, j))
        
        dirs = [(0, 1), (1,0), (-1, 0), (0, -1)]

        def isInBounds(i, j):
            return 0 <= i < m and 0 <= j < n
        
        res = 0
        d = [[inf for _ in range(n)] for _ in range(m)]

        while heap:
            max_height_so_far, i, j = heappop(heap)
            if d[i][j] <max_height_so_far:
                continue

            for x, y in dirs:
                ii, jj = i + x, j + y
                if isInBounds(ii, jj) and (ii, jj) not in border and (dd := max(max_height_so_far, A[ii][jj])) < d[ii][jj]:
                    d[ii][jj] = dd
                    res += max(0, max_height_so_far - A[ii][jj])
                    heappush(heap, (dd, ii, jj))

        return res