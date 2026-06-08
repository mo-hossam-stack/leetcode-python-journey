# Problem: 220. Contains Duplicate III
# LeetCode: https://leetcode.com/problems/contains-duplicate-iii/
# Difficulty: Hard

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        if indexDiff <= 0 or valueDiff < 0:
            return False

        width = valueDiff + 1
        buckets = {}

        def bucket_id(x: int) -> int:
            return x // width

        for i, x in enumerate(nums):
            bid = bucket_id(x)

            if bid in buckets:
                return True

            if bid - 1 in buckets and abs(x - buckets[bid - 1]) <= valueDiff:
                return True
            if bid + 1 in buckets and abs(x - buckets[bid + 1]) <= valueDiff:
                return True

            buckets[bid] = x

            if i >= indexDiff:
                old = nums[i - indexDiff]
                del buckets[bucket_id(old)]

        return False
