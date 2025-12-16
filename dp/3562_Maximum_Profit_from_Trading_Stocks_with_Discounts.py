# Problem: Maximum Profit from Trading Stocks with Discounts
# LeetCode: https://leetcode.com/problems/maximum-profit-from-trading-stocks-with-discounts/
# Difficulty: Hard

def merge(a, b):
    n = len(a)
    arr = [0] * n
    for i in range(n):
        for j in range(n-i):
            arr[i + j] = max(arr[i+j] , a[i] + b[j] )
    return arr

class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        adj = defaultdict(list)
        for a,b in hierarchy:
            adj[ a-1].append(b-1)

        def dfs(node):
            dp0 = [0] * (budget +1)
            dp1 = [0] * (budget +1)

            for nei in adj[node]:
                nei0 , nei1 =dfs(nei)
                dp0 = merge(dp0 ,nei0)
                dp1 = merge(dp1 , nei1)
            copy0 = dp0[:]
            copy1 = dp0[:]

            cost = present[node]
            for b in range(cost, budget +1):
                copy0[b] = max(copy0[b], dp1[b -cost]+future[node] - cost)

            cost //=2
            for b in range(cost, budget+ 1):
                copy1[b] = max(copy1[b], dp1[b -cost]+future[node] - cost)
            return copy0, copy1
        return dfs(0)[0][-1]
