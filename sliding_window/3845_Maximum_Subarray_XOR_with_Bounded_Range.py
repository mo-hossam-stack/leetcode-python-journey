# Problem: 3845. Maximum Subarray XOR with Bounded Range
# LeetCode: https://leetcode.com/problems/maximum-subarray-xor-with-bounded-range/
# Difficulty: Hard

from collections import deque

class Solution:
    def maxXor(self, nums: list[int], k: int) -> int:

        max_deque, min_deque = deque(), deque()
        ans, l, n = 0, 0, len(nums)
        max_bit_len = max(num.bit_length() for num in nums)
        trie = {1 << i: -1 for i in range(max_bit_len+2)}
        pref = 1 << (max_bit_len + 1)
        for r in range(n):
            while max_deque and nums[max_deque[-1]] <= nums[r]:
                max_deque.pop()
            while min_deque and nums[min_deque[-1]] >= nums[r]:
                min_deque.pop()
            max_deque.append(r)
            min_deque.append(r)

            while nums[max_deque[0]] - nums[min_deque[0]] > k:
                if max_deque[0] == l:
                    max_deque.popleft()
                if min_deque[0] == l:
                    min_deque.popleft()
                l += 1

            pref ^= nums[r]
            for i in range(max_bit_len):
                trie[pref >> i] = r

            pref_left = 1
            for i in range(max_bit_len, -1, -1):
                pref_left <<= 1
                mask = (pref >> i) & 1
                max_xor = pref_left | mask ^ 1
                if trie.get(max_xor, -2) >= l-1:
                    pref_left = max_xor
                else:
                    pref_left |= mask
            ans = max(ans, pref_left ^ pref)
        return ans
