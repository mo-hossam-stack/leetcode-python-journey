# Problem: String to Integer (atoi)
# LeetCode: https://leetcode.com/problems/string-to-integer-atoi/
# Difficulty: Medium

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0

        sign, i, res = 1, 0, 0

        if s[0] == '-':
            sign = -1
            i += 1
        elif s[0] == '+':
            i += 1

        while i < len(s) and s[i].isdigit():
            res = res * 10 + int(s[i])

            if sign * res > 2**31 - 1:
                return 2**31 - 1
            if sign * res < -2**31:
                return -2**31

            i += 1

        return sign * res
