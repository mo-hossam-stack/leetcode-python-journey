# Problem: 486. Predict the Winner
# LeetCode: https://leetcode.com/problems/predict-the-winner/
# Difficulty: Medium

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [0] * n

        for left in range(n - 1, -1, -1):
            dp[left] = nums[left]

            for right in range(left + 1, n):
                dp[right] = max(
                    nums[left] - dp[right],
                    nums[right] - dp[right - 1]
                )

        return dp[n - 1] >= 0
