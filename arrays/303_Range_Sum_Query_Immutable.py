# Problem: Range Sum Query - Immutable
# LeetCode: https://leetcode.com/problems/range-sum-query-immutable/
# Difficulty: Easy

class NumArray:

    def __init__(self, nums):
        self.accu_sum = [0]
        for num in nums:
            self.accu_sum.append(self.accu_sum[-1] + num)

    def sumRange(self, left, right):
        return self.accu_sum[right + 1] - self.accu_sum[left]