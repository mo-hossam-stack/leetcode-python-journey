# Problem: Maximum Square Area by Removing Fences From a Field
# LeetCode: https://leetcode.com/problems/maximum-square-area-by-removing-fences-from-a-field/
# Difficulty: Medium

class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        h = [1] + hFences + [m]
        v = [1] + vFences + [n]

        heights = set(abs(h[i] - h[j]) for i in range(len(h)) for j in range(i + 1, len(h)))
        widths = set(abs(v[i] - v[j]) for i in range(len(v)) for j in range(i + 1, len(v)))
        
        MOD = 10**9 + 7
        res = -1
        for height in heights:
            if height in widths:
                res = max(res, height * height)

        return res % MOD if res >= 0 else -1
