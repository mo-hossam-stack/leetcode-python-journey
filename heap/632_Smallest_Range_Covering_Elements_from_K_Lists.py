# Problem: 632. Smallest Range Covering Elements from K Lists
# LeetCode: https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/
# Difficulty: Hard

import heapq

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        min_heap = []
        current_max = float('-inf')  
        
        for i in range(len(nums)):
            heapq.heappush(min_heap, (nums[i][0], i, 0)) 
            current_max = max(current_max, nums[i][0]) 
        
        result_range = [-10**5, 10**5]
        
        while min_heap:
            current_min, list_idx, elem_idx = heapq.heappop(min_heap)
            if current_max - current_min < result_range[1] - result_range[0]:
                result_range = [current_min, current_max]
            
            if elem_idx + 1 == len(nums[list_idx]):
                break
            
            next_elem = nums[list_idx][elem_idx + 1]
            heapq.heappush(min_heap, (next_elem, list_idx, elem_idx + 1))
            
            current_max = max(current_max, next_elem)
        
        return result_range
