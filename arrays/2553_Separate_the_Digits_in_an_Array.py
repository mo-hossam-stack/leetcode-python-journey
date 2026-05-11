# Problem: 2553. Separate the Digits in an Array
# LeetCode: https://leetcode.com/problems/separate-the-digits-in-an-array/
# Difficulty: Easy
class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []
        for x in nums:
            tmp = []
            while x > 0:
                tmp.append(x % 10)
                x //= 10
            res.extend(tmp[::-1])
        return res
