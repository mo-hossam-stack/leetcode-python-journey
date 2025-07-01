# Problem: 3Sum
# LeetCode: https://leetcode.com/problems/3sum/description/
# Difficulty: medium

class Solution:
    def threeSum(self, nums):
        triples = []
        nums.sort()
        for i, val in enumerate(nums):
            if i and val == nums[i - 1]:
                continue
            
            left, right = i + 1, len(nums) - 1
            while left < right:
                currentsum = val + nums[left] + nums[right]
                if currentsum > 0:
                    right -= 1
                elif currentsum < 0:
                    left += 1
                else:
                    triples.append([val, nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
        return triples