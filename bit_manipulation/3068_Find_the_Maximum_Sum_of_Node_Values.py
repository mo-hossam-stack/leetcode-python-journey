# Problem: Find the Maximum Sum of Node Values  
# LeetCode: https://leetcode.com/problems/find-the-maximum-sum-of-node-values/  
# Difficulty: Hard  

class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        n = len(nums)
        diff = [0] *n
        for i in range(n): diff[i] = (nums[i] ^ k) - nums[i]
        diff.sort(reverse=True)

        total = sum(nums)
        for i in range(1, n ,2):
            pair = diff[i] + diff[i-1]
            if pair >0:
                total += pair
        return total
