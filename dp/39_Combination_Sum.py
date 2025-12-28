# Problem: Combination Sum
# LeetCode: https://leetcode.com/problems/combination-sum/
# Difficulty: Medium

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(start: int, remaining: int, path: List[int]):
            if remaining == 0:
                res.append(path[:])
                return
            if remaining < 0:
                return

            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, remaining - candidates[i], path)
                path.pop()

        backtrack(0, target, [])
        return res
