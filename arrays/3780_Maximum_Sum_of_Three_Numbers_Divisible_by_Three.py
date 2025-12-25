# Problem: Maximum Sum of Three Numbers Divisible by Three
# LeetCode: https://leetcode.com/problems/maximum-sum-of-three-numbers-divisible-by-three/
# Difficulty: Medium

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        n = len(nums)

        zero_mod = [num for num in nums if num % 3 ==0]
        one_mod = [num for num in nums if num%3 ==1]
        two_mod = [num for num in nums if num% 3==2]

        zero_mod.sort()
        one_mod.sort()
        two_mod.sort()

        res = 0
        if zero_mod and one_mod and two_mod:
            res = max(res, zero_mod[-1] +one_mod[-1] + two_mod[-1])

        if len(zero_mod) >=3:
            res = max(res,sum(zero_mod[-3:]))
                
        if len(one_mod) >=3:
            res = max(res,sum(one_mod[-3:]))

        if len(two_mod) >=3:
            res = max(res,sum(two_mod[-3:]))

        return res
