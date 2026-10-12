# Problem: 2897. Apply Operations on Array to Maximize Sum of Squares
# LeetCode: https://leetcode.com/problems/apply-operations-on-array-to-maximize-sum-of-squares/
# Difficulty: Medium
class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        b = [0] * 30
        ans, mod = 0, 1000000007

        for x in nums:
            for i in range(30):
                if x & (1 << i):
                    b[i] += 1

        for _ in range(k):
            x = 0
            for i in range(30):
                if b[i] > 0:
                    x |= 1 << i
                    b[i] -= 1
            ans = (ans + x * x) % mod

        return ans
