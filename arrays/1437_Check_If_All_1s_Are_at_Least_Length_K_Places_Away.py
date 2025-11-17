# Problem: Check If All 1's Are at Least Length K Places Away
# LeetCode: https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/
# Difficulty: Easy

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        prev = -1
        for i in range(n):
            if nums[i] == 1:
                if prev != -1 and i - prev - 1 < k:
                    return False
                prev = i 
        return True