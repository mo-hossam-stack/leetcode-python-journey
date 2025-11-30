Problem: Minimum Absolute Distance Between Mirror Pairs
LeetCode: https://leetcode.com/problems/minimum-absolute-distance-between-mirror-pairs/
Difficulty: Medium

class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        n = len(nums)

        def rev(s):
            return int(str(s)[::-1])
        
        prev_rev = {}
        res = inf
        for i in range(n):
            if nums[i] in prev_rev:
                res = min(res, i - prev_rev[nums[i]])

            prev_rev[rev(nums[i])] = i

        return res if res != inf else -1
