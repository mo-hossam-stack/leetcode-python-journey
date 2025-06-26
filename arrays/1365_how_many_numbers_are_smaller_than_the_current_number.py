# Problem: How Many Numbers Are Smaller Than the Current Number
# LeetCode: https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
# Difficulty: Easy


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp = sorted(nums)
        d={} # val, index
        for i,num in enumerate(temp):
            if num not in d:
                d[num] = i
        ret=[]
        for i in nums:
            ret.append(d[i])
        return ret
