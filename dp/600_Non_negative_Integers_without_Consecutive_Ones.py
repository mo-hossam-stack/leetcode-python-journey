# Problem: 600. Non-negative Integers without Consecutive Ones
# LeetCode: https://leetcode.com/problems/non-negative-integers-without-consecutive-ones/
# Difficulty: Hard

class Solution:
    def findIntegers(self, n: int) -> int:
        def solve(idx, tight, prevOne, dp):
            if idx == len(num):
                return 1

            state = (idx, tight, prevOne)
            if state in dp:
                return dp[state]

            ub = int(num[idx]) if tight else 1
            res = 0

            for digit in range(0, ub + 1):
                if digit == 1 and prevOne:
                    continue

                res += solve(
                    idx + 1,
                    tight and digit == ub,
                    digit == 1,
                    dp
                )

            dp[state] = res
            return res

        num = bin(n)[2:]
        dp = {}
        return solve(0, True, False, dp)
