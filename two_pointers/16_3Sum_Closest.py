# Problem: 3Sum Closest
# LeetCode: https://leetcode.com/problems/3sum-closest/
# Difficulty: Medium

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        res = 0
        min_dis = float("inf")
        for i in range(n):
            l = i + 1
            r = n - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                curr_dis = abs(target - s)
                if curr_dis < min_dis:
                    min_dis = curr_dis
                    res = s
                if s < target:
                    l += 1
                else:
                    r -= 1
        return res
