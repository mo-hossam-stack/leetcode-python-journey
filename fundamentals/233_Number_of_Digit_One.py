# Problem: 233. Number of Digit One
# LeetCode: https://leetcode.com/problems/number-of-digit-one/
# Difficulty: Hard
class Solution:
    def countDigitOne(self, n: int) -> int:
        if n <= 0:
            return 0
        if n < 10:
            return 1

        pow10 = 1
        while pow10 * 10 <= n:
            pow10 *= 10

        high = n // pow10
        rest = n % pow10

        if high == 1:
            highest_contribution = rest + 1
        else:
            highest_contribution = pow10

        return (
            high * self.countDigitOne(pow10 - 1)
            + highest_contribution
            + self.countDigitOne(rest)
        )
