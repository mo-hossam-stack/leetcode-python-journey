# Problem: 1979. Find Greatest Common Divisor of Array
# LeetCode: https://leetcode.com/problems/find-greatest-common-divisor-of-array/
# Difficulty: Easy

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        return gcd(min(nums), max(nums))
