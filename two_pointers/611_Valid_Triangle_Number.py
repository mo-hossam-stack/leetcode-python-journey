# Problem: Valid Triangle Number
# LeetCode: https://leetcode.com/problems/valid-triangle-number/
# Difficulty: Medium

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        nums.sort()
        for k in range(n):
            i = 0
            j = k - 1
            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    res += j - i
                    j -= 1
                else:
                    i += 1
        return res