# Problem: Binary Prefix Divisible By 5  
# LeetCode: https://leetcode.com/problems/binary-prefix-divisible-by-5/  
# Difficulty: Easy  

class Solution:  
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:  
        res = []  
        prev = 0  
        for num in nums:  
            prev = (prev << 1) | num  
            res.append(prev % 5 == 0)  
        return res  
