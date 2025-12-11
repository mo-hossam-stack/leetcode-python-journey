# Problem: Sort Integers by Binary Reflection
# LeetCode: https://leetcode.com/problems/sort-integers-by-binary-reflection/description/
# Difficulty: easy

class Solution:
    def sortByReflection(self, nums: List[int]) -> List[int]:
        nums = [(int(bin(num)[2:][::-1]), num) for num in nums]
        nums.sort()
        return [a[1] for a in nums]