# Problem: Construct the Minimum Bitwise Array II
# LeetCode: https://leetcode.com/problems/construct-the-minimum-bitwise-array-ii/
# Difficulty: Medium

class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            res = -1
            d = 1
            while (nums[i] & d) != 0:
                res = nums[i] - d
                d <<= 1
            nums[i] = res
        return nums
