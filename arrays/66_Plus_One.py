# Problem: Plus One
# LeetCode: https://leetcode.com/problems/plus-one/
# Difficulty: Easy

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        h = map(str, digits)
        n = int("".join(h)) + 1
        res = list(str(n))

        return list(map(int , res))

    def plusOne(self, digits: List[int]) -> List[int]:

        n = len(digits)
        for i in range(n-1 , -1 , -1):
            digits[i] += 1
            if digits[i] < 10:return digits
            digits[i] %=10

        return [1] + digits
