# Problem: 1404. Number of Steps to Reduce a Number in Binary Representation to One
# LeetCode: https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/
# Difficulty: Medium

class Solution:
    def divide_by_two(self, s):
        s.pop()

    def add_one(self, s):
        i = len(s) - 1

        while i >= 0 and s[i] != "0":
            s[i] = "0"
            i -= 1

        if i < 0:
            s.insert(0, "1")
        else:
            s[i] = "1"

    def numSteps(self, s: str) -> int:
        s = list(s)
        ans = 0

        while len(s) > 1:
            N = len(s)

            if s[N - 1] == "0":
                self.divide_by_two(s)
            else:
                self.add_one(s)

            ans += 1

        return ans
