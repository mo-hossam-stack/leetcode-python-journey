# Problem: 3876. Construct Uniform Parity Array II
# LeetCode: https://leetcode.com/problems/construct-uniform-parity-array-ii/
# Difficulty: Medium
class Solution:
    def uniformArray(self, nums):
        smallestOdd = float('inf')

        for num in nums:
            if num&1:
                smallestOdd = min(smallestOdd, num)


        if smallestOdd == float('inf'):
            return True

        ok = True
        for num in nums:
            ok &= not (num % 2 == 0 and num <= smallestOdd)
        
        return ok
