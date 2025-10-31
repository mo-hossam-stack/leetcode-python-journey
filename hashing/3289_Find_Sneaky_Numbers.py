# Problem: Find the Sneaky Numbers
# LeetCode: https://leetcode.com/problems/find-the-sneaky-numbers/
# Difficulty: Easy

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        s = set()
        ret = []
        for num in nums:
            if num in s:
                ret.append(num)
            else:
                s.add(num)
        return ret