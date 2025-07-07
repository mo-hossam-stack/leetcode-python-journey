# Problem: Count Number of Pairs With Absolute Difference K
# LeetCode: https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/
# Difficulty: Easy


class Solution:
    def countKDifference(self, nums, k):
        h = defaultdict(int)
        count = 0
        for num in nums:
            count += h[num - k] + h[num + k]
            h[num] += 1
        return count