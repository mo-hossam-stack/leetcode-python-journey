# Problem: 3718. Smallest Missing Multiple of K
# LeetCode: https://leetcode.com/problems/smallest-missing-multiple-of-k/
# Difficulty: Easy
from typing import List

class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        present = set(nums)

        ans = k

        while ans in present:
            ans += k

        return ans
