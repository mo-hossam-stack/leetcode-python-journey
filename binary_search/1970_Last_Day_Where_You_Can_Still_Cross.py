# Problem: Last Day Where You Can Still Cross
# LeetCode: https://leetcode.com/problems/last-day-where-you-can-still-cross/
# Difficulty: Hard

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        def solve(target):
            grid = [[0] * col for _ in range(row)]

            for i in range(target):
                r , c = cells[i]
                grid[r-1][c-1] = 1

            q = deque([])

            seen = set()
            for i in range(col):
                if grid[0][i] == 0:
                    q.append((0,i))
                    seen.add((0,i))

            while q:
                r , c = q.popleft()
                if r == row -1:return True
                for nr , nc in ((r+1 , c) , (r-1 , c),(r,c- 1) ,(r,c+1)):
                    if nr <0 or nr >= row or nc<0 or nc >= col or (nr , nc) in seen:continue
                    if grid[nr][nc] == 0:
                        q.append((nr,nc))
                        seen.add((nr,nc))

            return False
        
        l = 0
        h = len(cells) - 1
        while l <h:
            mid =l + (h - l + 1) //2 # when need it rounded up so i add 1
            if solve(mid): l = mid
            else:
                h = mid - 1
        return l
