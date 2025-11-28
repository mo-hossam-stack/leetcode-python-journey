# Problem: Maximum  Number of K-Divisible Components
# LeetCode: https://leetcode.com/problems/maximum-number-of-k-divisible-components/
# Difficulty: Hard

class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        graph =defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        res=0
        def dfs(node, parent):
            nonlocal res
            
            total=values[node]

            for nei in graph[node]:
                if nei!= parent:
                    total+=dfs(nei, node)

            if total%k==0:
                res+= 1

            return total

        dfs(0, -1)
        return res
