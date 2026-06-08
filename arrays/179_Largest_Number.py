# Problem: 179. Largest Number
# LeetCode: https://leetcode.com/problems/largest-number/
# Difficulty: Medium

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        arr = list(map(str, nums))

        from functools import cmp_to_key

        def cmp(a: str, b: str) -> int:
            ab = a + b
            ba = b + a
            if ab > ba:
                return -1
            if ab < ba:
                return 1
            return 0

        arr.sort(key=cmp_to_key(cmp))

        if arr[0] == "0":
            return "0"

        return "".join(arr)
