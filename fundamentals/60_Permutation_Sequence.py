# Problem: 60. Permutation Sequence
# LeetCode: https://leetcode.com/problems/permutation-sequence/
# Difficulty: Hard

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [str(i) for i in range(1, n + 1)]
        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i
        
        k -= 1  
        ans = []
        for i in range(n, 0, -1):
            idx = k // fact[i - 1]
            ans.append(nums[idx])
            nums.pop(idx)
            k %= fact[i - 1]
        return ''.join(ans)
