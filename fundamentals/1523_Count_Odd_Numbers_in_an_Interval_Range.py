#Problem: Count Odd Numbers in an Interval Range
#LeetCode: https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/description/
#Difficulty: Easy

class Solution:
    def countOdds(self, l, h) -> int:
        return (h-l)//2 + (l % 2 or h % 2)