# Problem: 1494. Parallel Courses II
# LeetCode: https://leetcode.com/problems/parallel-courses-ii/
# Difficulty: Hard

class Solution:
    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
        post = collections.defaultdict(list)
        degree = [0 for _ in range(n)]
        for a, b in relations:
            degree[b - 1] += 1
            post[a - 1].append(b - 1)
        
        @cache
        def dp(mask: int) -> int:
            if mask == (1 << n) - 1: return 0
            take = []
            for i in range(n):
                if not mask & (1 << i) and degree[i] == 0: take.append(i)

            ans = float("inf")
            for k_take in combinations(take, min(k, len(take))):
                new_mask = mask
                for i in k_take:
                    new_mask |= 1 << i
                    for next in post[i]: degree[next] -= 1
                ans  = min(ans, 1 + dp(new_mask))
                for i in k_take:
                    for next in post[i]: degree[next] += 1
            return ans
        
        return dp(0)
