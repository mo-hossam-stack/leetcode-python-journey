# Problem: Design an Ordered Stream
# LeetCode: https://leetcode.com/problems/design-an-ordered-stream/
# Difficulty: Easy

class OrderedStream:
    def __init__(self, n: int):
        self.ptr = 1
        self.cache = {}

    def insert(self, idKey: int, value: str) -> List[str]:
        self.cache[idKey] = value
        res = []
        while self.ptr in self.cache:
            res.append(self.cache[self.ptr])
            self.ptr += 1
        return res
