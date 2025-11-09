# Problem: Minimum One Bit Operations to Make Integers Zero
# LeetCode: https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/
# Difficulty: Hard

class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        if n==0:return 0
        """
        last = 0
        curr = n
        while curr:
            curr //=2
            last+=1
        last -=1
        """
        last = n.bit_length() - 1
        return 2** (last + 1) - 1 - self.minimumOneBitOperations(n ^ 2**last)