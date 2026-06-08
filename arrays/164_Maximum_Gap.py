# Problem: 164. Maximum Gap
# LeetCode: https://leetcode.com/problems/maximum-gap/
# Difficulty: Medium

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        maxGap=0
        nums.sort()
        for i in range(1,len(nums)):
            cur=abs(nums[i]-nums[i-1])
            maxGap=max(maxGap,cur)
        return 0 if len(nums)<2 else maxGap
