# Problem: 3514. Number of Unique XOR Triplets II
# LeetCode: https://leetcode.com/problems/number-of-unique-xor-triplets-ii/
# Difficulty: Medium

class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        MAX_XOR = 2048

        pair_xor = [False] * MAX_XOR
        triplet_xor = [False] * MAX_XOR

        n = len(nums)

        for i in range(n):
            for j in range(i, n):
                pair_xor[nums[i] ^ nums[j]] = True

        for x in range(MAX_XOR):
            if not pair_xor[x]:
                continue

            for v in nums:
                triplet_xor[x ^ v] = True

        return sum(triplet_xor)
