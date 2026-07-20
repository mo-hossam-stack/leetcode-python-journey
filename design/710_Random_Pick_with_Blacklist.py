# Problem: 710. Random Pick with Blacklist
# LeetCode: https://leetcode.com/problems/random-pick-with-blacklist/
# Difficulty: Hard

from typing import List
from random import randint

class Solution:
    def __init__(self, N: int, blacklist: List[int]):
        blacklist = set(blacklist)
        self.N = N - len(blacklist)
        key = [x for x in blacklist if x < N - len(blacklist)]
        val = [x for x in range(N - len(blacklist), N) if x not in blacklist]
        self.mapping = dict(zip(key, val))

    def pick(self) -> int:
        i = randint(0, self.N - 1)
        return self.mapping.get(i, i)

# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()
