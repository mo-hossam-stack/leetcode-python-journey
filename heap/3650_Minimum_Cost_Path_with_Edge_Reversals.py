# Problem: Minimum Cost Path with Edge Reversals
# LeetCode: https://leetcode.com/problems/minimum-cost-path-with-edge-reversals/
# Difficulty: Medium

class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for a, b, w in edges:
            adj[a].append((b, w))
            adj[b].append((a, w * 2))

        dist = [0] + [inf] * (n - 1)
        heap = []
        heapq.heappush(heap, (0, 0))

        while heap:
            w, node = heapq.heappop(heap)
            for nei, nw in adj[node]:
                if w + nw < dist[nei]:
                    dist[nei] = w + nw
                    heapq.heappush(heap, (w + nw, nei))

        return dist[n - 1] if dist[n - 1] != inf else -1
