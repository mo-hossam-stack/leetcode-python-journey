# Problem: 1524. Number of Sub-arrays With Odd Sum
# LeetCode: https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/
# Difficulty: Medium
class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        odd = even = ans = 0

        for x in arr:
            if x % 2 == 1:
                odd, even = even + 1, odd
            else:
                even += 1
            ans = (ans + odd) % MOD

        return ans
