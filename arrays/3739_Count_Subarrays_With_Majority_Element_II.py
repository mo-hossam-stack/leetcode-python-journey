# Problem: 3739. Count Subarrays With Majority Element II
# LeetCode: https://leetcode.com/problems/count-subarrays-with-majority-element-ii/
# Difficulty: Hard

class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        pref = n

        freq = [0] * (2 * n + 1)
        freq[n] = 1

        less = 0
        ans = 0

        for num in nums:
            if num == target:
                less += freq[pref]
                pref += 1
            else:
                pref -= 1
                less -= freq[pref]

            freq[pref] += 1
            ans += less

        return ans
