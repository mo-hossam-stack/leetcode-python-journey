#Problem: Count Elements With at Least K Greater Values
#LeetCode: https://leetcode.com/problems/count-elements-with-at-least-k-greater-values/description/
#Difficulty: Medium

class Solution:
    def countElements(self, nums: List[int], k: int) -> int:
        if k==0:return len(nums)
        nums.sort()

        n = len(nums)
        threshold = nums[n - k]
        
        res = 0
        for num in nums:
            if num < threshold:res+=1
        return res
