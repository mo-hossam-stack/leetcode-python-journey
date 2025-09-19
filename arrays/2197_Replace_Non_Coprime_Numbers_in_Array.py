# Problem: Replace Non-Coprime Numbers in Array
# LeetCode: https://leetcode.com/problems/replace-non-coprime-numbers-in-array/
# Difficulty: Hard

class Solution:
    # It can be shown that replacing adjacent non-coprime numbers in any arbitrary order 
    # will lead to the same result.
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = []
        for num in nums:
            while stack and gcd(stack[-1], num) > 1:
                num = lcm(stack.pop(), num)
            stack.append(num)
        return stack