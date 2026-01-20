# Problem: Construct the Minimum Bitwise Array I
# LeetCode: https://leetcode.com/problems/construct-the-minimum-bitwise-array-i/
# Difficulty: Easy

class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            temp = num
            ans = -1
            
            for j in range(1, temp):
                if (j | (j + 1)) == temp:
                    ans = j
                    break
            res.append(ans)
        return res
