# Problem: 22. Generate Parentheses
# LeetCode: https://leetcode.com/problems/generate-parentheses/
# Difficulty: Medium
class Solution: 
    def generateParenthesis(self, n: int) -> list[str]: 
        ans = []
        cur = []
        def dfs(open, close):
            if open == 0 and close == 0:
                ans.append(''.join(cur))
                return
            if open > 0:
                cur.append('(')
                dfs(open - 1, close)
                cur.pop()
            if close > open:
                cur.append(')')
                dfs(open, close - 1)
                cur.pop()
        dfs(n, n)
        return ans
