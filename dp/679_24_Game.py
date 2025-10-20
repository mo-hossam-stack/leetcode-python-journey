# Problem: 24 Game  
# LeetCode: https://leetcode.com/problems/24-game/  
# Difficulty: Hard  

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        def dfs(nums): # o(1) solution however it 4!* 6^4 
            if len(nums) == 1:
                return isclose(nums[0], 24)
            n = len(nums)
            for i in range(n):
                for j in range(n):
                    if i != j:
                        base = [nums[k] for k in range(n) if k != i and k != j]
                        if dfs(base + [nums[i] + nums[j]]): return True
                        if dfs(base + [nums[i] - nums[j]]): return True
                        if dfs(base + [nums[i] * nums[j]]): return True
                        if nums[j] != 0 and dfs(base + [nums[i] / nums[j]]): return True
                        if dfs(base + [nums[j] - nums[i]]): return True
                        if nums[i] != 0 and dfs(base + [nums[j] + nums[i]]): return True
            return False
        return dfs(cards)
