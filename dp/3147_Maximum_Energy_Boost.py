# Problem: Maximum Energy Boost
# LeetCode: https://leetcode.com/problems/maximum-energy-boost/
# Difficulty: Medium

class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        for i in range(k, len(energy)):
            energy[i] = max(energy[i], energy[i] + energy[i - k])
        return max(energy[-k:])