# Problem: 462. Minimum Moves to Equal Array Elements II
# LeetCode: https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/
# Difficulty: Medium
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        def quickselect(a, k):
            while True:
                if len(a) <= 1:
                    return a[0]
                p = a[random.randrange(len(a))]
                lo = [x for x in a if x < p]
                if k < len(lo):
                    a = lo
                    continue
                hi = [x for x in a if x > p]
                if k >= len(a) - len(hi):
                    k -= len(a) - len(hi)
                    a = hi
                    continue
                return p  

        med = quickselect(nums, len(nums) // 2)
        return sum(abs(x - med) for x in nums)
