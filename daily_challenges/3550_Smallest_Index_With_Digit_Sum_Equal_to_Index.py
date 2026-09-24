# Problem: 3550. Smallest Index With Digit Sum Equal to Index
# LeetCode: https://leetcode.com/problems/smallest-index-with-digit-sum-equal-to-index/
# Difficulty: Easy
class Solution:
    def smallestIndex(self, nums):

        for i in range(len(nums)):
            x = nums[i]
            tot = 0

            while x > 0:
                tot += x % 10
                x //= 10

            if tot == i:
                return i

        return -1
