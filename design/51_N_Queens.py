# Problem: 51. N-Queens
# LeetCode: https://leetcode.com/problems/n-queens/
# Difficulty: Hard

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtrack(r):
            # Base case: if we've placed queens in all rows successfully
            if r == n:
                copy = board[:]
                sol = []
                for c in copy:
                    sol.append("".join(c[:]))
                ans.append(sol)
                return

            for c in range(n):
                if c in placedCol or r + c in placedPos or r - c in placedNeg:
                    continue

                board[r][c] = "Q"
                placedCol.add(c)
                placedPos.add(r + c)
                placedNeg.add(r - c)

                backtrack(r + 1)

                board[r][c] = "."
                placedCol.remove(c)
                placedPos.remove(r + c)
                placedNeg.remove(r - c)

        board = [["."] * n for _ in range(n)]
        
        placedCol = set() 
        placedPos = set()
        placedNeg = set()
        ans = []
        
        backtrack(0)
        return ans
