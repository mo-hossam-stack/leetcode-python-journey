# Problem: Squares of a Sorted Array
# LeetCode: https://leetcode.com/problems/squares-of-a-sorted-array/description/
# Difficulty: easy

class Solution:
    def sortedSquares(self, nums):
        answer = []
        l , r = 0 , len(nums) - 1
        while l <= r:
            left , right = abs(nums[l]) , abs(nums[r])
            if right > left:
                answer.insert(0, right * right)
                r -= 1
            else:
                answer.insert(0, left * left)
                l += 1
        return answer