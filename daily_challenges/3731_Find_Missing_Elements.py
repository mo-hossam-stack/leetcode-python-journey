# Problem: 3731. Find Missing Elements
# LeetCode: https://leetcode.com/problems/find-missing-elements/
# Difficulty: Easy

class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums = set(nums)
        ret = []
        for i in range(min(nums)  + 1, max(nums)):
            if i not in nums:
                ret.append(i)
        return ret
