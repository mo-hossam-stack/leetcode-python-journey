# Problem: 128. Longest Consecutive Sequence
# LeetCode: https://leetcode.com/problems/longest-consecutive-sequence/
# Difficulty: Medium
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashmap=set(nums)
        max_length=0
        for num in hashmap:
            if num-1 not in hashmap:
                current=num
                length=0
                while current in hashmap:
                    length+=1
                    current+=1
                max_length=max(max_length,length)
        return max_length
