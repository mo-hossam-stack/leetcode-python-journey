# Problem: 2492. Minimum Score of a Path Between Two Cities
# LeetCode: https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/
# Difficulty: Medium

class Solution:
    def minScore(self, n: int, roads: list[list[int]]) -> int:
        root = list(range(n + 1))

        def find(i: int) -> int:
            root[i] = find(root[i]) if root[i] != i else i
            return root[i]

        for x, y, _ in roads:
            root[find(x)] = find(y)

        res, g1 = 10001, find(1)
        for x, _, d in roads:
            if find(x) == g1:
                res = min(res, d)

        return res
