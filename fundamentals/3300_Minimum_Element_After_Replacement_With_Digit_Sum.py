# Problem: 3300. Minimum Element After Replacement With Digit Sum
# LeetCode: https://leetcode.com/problems/minimum-element-after-replacement-with-digit-sum/
# Difficulty: Easy
class Solution:
    def minElement(self, nums: List[int]) -> int:
        def sum_dig(n):
            sum = 0
            while n > 0:
                sum += n%10
                n //= 10
            return sum
        mn = 100
        for num in nums:
            mn = min(mn , sum_dig(num))
        return mn
