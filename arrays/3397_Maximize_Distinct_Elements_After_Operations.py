# Problem: Maximize Distinct Elements After Operations  
# LeetCode: https://leetcode.com/problems/maximize-distinct-elements-after-operations/  
# Difficulty: Medium  

class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        nums[0]-= k
        for i in range(1,len(nums)):
            if nums[i]- k>nums[i - 1]: 
                nums[i] -=k
            elif nums[i]-k <= nums[i - 1] < nums[i] + k:
                nums[i]= nums[i- 1] + 1
            else:
                nums[i] += k
        return len(set(nums))
