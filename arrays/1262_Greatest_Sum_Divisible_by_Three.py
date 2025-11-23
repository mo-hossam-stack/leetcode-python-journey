# Problem: Greatest Sum Divisible by Three
# LeetCode: https://leetcode.com/problems/greatest-sum-divisible-by-three/
# Difficulty: Medium

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        r1 = sorted([x for x in nums if x%3==1])
        r2 = sorted([x for x in nums if x%3==2])
        s= sum(nums)
        rm = float('inf')
        if s % 3 != 0:
            if s % 3==1:
                if r1 :rm = min(rm, r1[0])
                if len(r2) >= 2 :rm = min(rm, r2[0] + r2[1])
            else:
                if len(r1) >=2 : rm = min(rm, r1[0] + r1[1])
                if r2 : rm = min(rm, r2[0])
        
        return s if rm == float('inf') else s - rm
