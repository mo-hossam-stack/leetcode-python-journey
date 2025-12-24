# Problem: Minimum Number of Operations to Have Distinct Elements
# LeetCode: https://leetcode.com/problems/minimum-number-of-operations-to-have-distinct-elements/
# Difficulty: Medium

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        set_ = set()

        j = -1 
        n = len(nums)
        for i in range(n-1, -1, -1):
            if nums[i] in set_:
                j = i
                break

            set_.add(nums[i])

        return ceil((j+1) / 3)
