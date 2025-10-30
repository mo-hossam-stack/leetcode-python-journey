# Problem: Count the Number of Valid Selections  
# LeetCode: https://leetcode.com/problems/count-the-number-of-valid-selections/  
# Difficulty: easy  

class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        s = 0
        for i in range(len(nums)):
            s += nums[i]
        t = r = 0
        for i in range(len(nums)):
            t += nums[i]
            if nums[i]==0:
                if (t == s - t):
                    r += 2
                elif (t == s - t + 1 or t == s - t - 1):
                    r+=1
        return r
