# Problem: Maximum Subgraph Score in a Tree
# LeetCode: https://leetcode.com/problems/maximum-subgraph-score-in-a-tree/
# Difficulty: Hard

class Solution:
    def maxSubgraphScore(self, n: int, edges: List[List[int]], good: List[int]) -> List[int]:
        adjList = defaultdict(list)

        for u, v in edges:
            adjList[u].append(v)

            adjList[v].append(u)

        dp = [0] * n
        def dfs1(node, par):
            dp[node] = 1 if good[node] else -1

            for nbr in adjList[node]:
                if nbr != par:
                    dfs1(nbr, node)
                    dp[node] += max(0, dp[nbr])

        dfs1(0, -1)
        ans = [0] * n

        def dfs2(node, par, parent_contrib):
            ans[node] = dp[node] + max(0, parent_contrib)
            for nbr in adjList[node]:
                if nbr != par:
                    node_contrib = dp[node] - max(0, dp[nbr]) + max(0, parent_contrib)

                    dfs2(nbr, node, node_contrib)
        dfs2(0, -1, 0)
        return ans
