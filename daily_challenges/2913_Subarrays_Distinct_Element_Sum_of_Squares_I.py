# Problem: 2913. Subarrays Distinct Element Sum of Squares I
# LeetCode: https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-i/
# Difficulty: Easy
class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        total = 0
        for i in range(len(nums)):
            seen = set()
            for x in nums[i:]:
                seen.add(x)
                total += len(seen) ** 2
        return total
