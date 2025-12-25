# Problem: Maximize Happiness of Selected Children
# LeetCode: https://leetcode.com/problems/maximize-happiness-of-selected-children/
# Difficulty: Medium

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        res = 0
        adjustment = 0
        for i in range(k):
            res += max(0, happiness[i] - adjustment)
            adjustment += 1
        return res
            
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        return sum(max(0, happiness[i]-i) for i in range(k))
            
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        res = 0
        for i in range(k):
            if happiness[i] - i <= 0: break
            res += happiness[i] - i
        return res
