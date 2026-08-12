# Problem: 1787. Make the XOR of All Segments Equal to Zero
# LeetCode: https://leetcode.com/problems/make-the-xor-of-all-segments-equal-to-zero/
# Difficulty: Medium
class Solution:
    def minChanges(self, nums, k):
        MASK_LIMIT = 1 << 10
        
        occurrences = defaultdict(Counter)
        for idx, num in enumerate(nums):
            occurrences[idx % k][num] += 1
        
        table = [[0] * MASK_LIMIT for _ in range(k + 1)]
        for i in range(1, MASK_LIMIT):
            table[0][i] = -float('inf')
        
        for i in range(1, k + 1):
            row_max = max(table[i - 1])
            
            for j in range(MASK_LIMIT):
                for bit in occurrences[i - 1]:
                    table[i][j] = max(table[i][j], row_max, table[i - 1][j ^ bit] + occurrences[i - 1][bit])
        
        return len(nums) - table[k][0]
