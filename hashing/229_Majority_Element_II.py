# Problem: 229. Majority Element II
# LeetCode: https://leetcode.com/problems/majority-element-ii/
# Difficulty: Medium

from collections import Counter
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        element_count = Counter(nums)
        
        majority_elements = []
        threshold = len(nums) // 3
        
        for element, count in element_count.items():
            if count > threshold:
                majority_elements.append(element)
        
        return majority_elements
