# Problem: 805. Split Array With Same Average
# LeetCode: https://leetcode.com/problems/split-array-with-same-average/
# Difficulty: Hard

class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        n = len(nums)
        
        if n == 1:
            return False
        
        def possible_sums(arr: List[int]) -> int:
            subset_sums = 1
            for a in arr:
                subset_sums |= (subset_sums << a)
            return (subset_sums - 1) ^ (1 << sum(arr))
        
        transformed_nums = [n * num - total_sum for num in nums]
        
        if 0 in transformed_nums:
            return True
        
        positives = [num for num in transformed_nums if num > 0]
        negatives = [-num for num in transformed_nums if num < 0]
        
        return bool(possible_sums(positives) & possible_sums(negatives))
