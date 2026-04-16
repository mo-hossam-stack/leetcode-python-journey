# Problem: 3488. Closest Equal Element Queries
# LeetCode: https://leetcode.com/problems/closest-equal-element-queries/
# Difficulty: Medium

class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        mp = defaultdict(list)

        for i in range(n):
            mp[nums[i]].append(i)

        ans = []

        for q in queries:
            v = mp[nums[q]]

            if len(v) == 1:
                ans.append(-1)
                continue

            pos = bisect_left(v, q)
            res = float('inf')

            left = v[(pos - 1) % len(v)]
            d1 = abs(q - left)
            res = min(res, min(d1, n - d1))

            right = v[(pos + 1) % len(v)]
            d2 = abs(q - right)
            res = min(res, min(d2, n - d2))

            ans.append(res)

        return ans
