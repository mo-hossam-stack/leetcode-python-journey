# Problem: Maximum Subarray Sum With Length Divisible by K
# LeetCode: https://leetcode.com/problems/maximum-subarray-sum-with-length-divisible-by-k/
# Difficulty: Medium


class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:

        res = -inf

        min_prefix_sum = defaultdict(lambda: inf)

        min_prefix_sum[0] = 0

        pref_sum = 0

        for i in range(len(nums)):

            pref_sum += nums[i]

            res = max(res, pref_sum - min_prefix_sum[((i+1) - k) % k])

            min_prefix_sum[(i+1) % k] = min(min_prefix_sum[(i+1) % k], pref_sum)

        

        return res

    

    def maxSubarraySum(self, nums: List[int], k: int) -> int:

        res = -inf

        min_prefix_sum = defaultdict(lambda: inf, {0:0})

        pref_sum = [0] + list(accumulate(nums))

        for l in range(1, len(nums)+1):

            res = max(res, pref_sum[l] - min_prefix_sum[(l - k) % k])

            min_prefix_sum[l % k] = min(min_prefix_sum[l % k], pref_sum[l])

        return res
