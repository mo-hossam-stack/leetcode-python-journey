# Problem: 295. Find Median from Data Stream
# LeetCode: https://leetcode.com/problems/find-median-from-data-stream/
# Difficulty: Hard

class MedianFinder:
    def __init__(self):
        self.lowerHalf = []  
        self.upperHalf = []  

    def addNum(self, num: int) -> None:
        heapq.heappush(self.lowerHalf, -num)

        heapq.heappush(self.upperHalf, -heapq.heappop(self.lowerHalf))

        if len(self.upperHalf) > len(self.lowerHalf):
            heapq.heappush(self.lowerHalf, -heapq.heappop(self.upperHalf))

    def findMedian(self) -> float:
        if len(self.lowerHalf) > len(self.upperHalf):
            return -self.lowerHalf[0]
        return (-self.lowerHalf[0] + self.upperHalf[0]) / 2.0