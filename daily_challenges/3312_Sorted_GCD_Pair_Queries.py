# Problem: 3312. Sorted GCD Pair Queries
# LeetCode: https://leetcode.com/problems/sorted-gcd-pair-queries/
# Difficulty: Hard

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        max_value = max(nums)
        freq = [0] * (max_value + 1)
        for i in nums:
            freq[i] += 1
        cnt = [0] * (max_value + 1)
        for j in range(max_value, 0, -1):
            total = 0
            for x in range(j, max_value + 1, j):
                total += freq[x]
            pairs = total * (total - 1) // 2
            
            for x in range(2 * j, max_value + 1, j):
                pairs -= cnt[x]
            cnt[j] = pairs
        pref = []
        vals = []
        s = 0
        for j in range(1, max_value + 1):
            if cnt[j]:
                s += cnt[j]
                pref.append(s)
                vals.append(j)
        res = []
        for q in queries:
            res.append(vals[bisect_left(pref, q + 1)])
        return res
