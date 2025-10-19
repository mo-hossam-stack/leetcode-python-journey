# Problem: Three Equal Parts  
# LeetCode: https://leetcode.com/problems/three-equal-parts/  
# Difficulty: Hard 

class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        total_ones = sum(arr)
        
        if total_ones == 0:
            return [0, len(arr) - 1]
        
        if total_ones % 3 != 0:
            return [-1, -1]
        
        ones_per_part = total_ones // 3
        first = second = third = -1
        count = 0
        
        # Locate first '1' in each part
        for i, bit in enumerate(arr):
            if bit == 1:
                count += 1
                if count == 1:
                    first = i
                elif count == ones_per_part + 1:
                    second = i
                elif count == 2 * ones_per_part + 1:
                    third = i
        
        # Compare parts
        n = len(arr)
        while third < n and arr[first] == arr[second] == arr[third]:
            first += 1
            second += 1
            third += 1
        
        if third == n:
            return [first - 1, second]
        
        return [-1, -1]
