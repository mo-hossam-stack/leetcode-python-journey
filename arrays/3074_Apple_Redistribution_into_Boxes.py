# Problem: Apple Redistribution into Boxes
# LeetCode: https://leetcode.com/problems/apple-redistribution-into-boxes/
# Difficulty: Easy

class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse=True)
        sum_ = sum(apple)
        i = 0
        while(sum_ > 0 and i < len(capacity)):
            sum_ -= capacity[i]
            i += 1
        return i