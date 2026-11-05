# Problem: 1385. Find the Distance Value Between Two Arrays
# LeetCode: https://leetcode.com/problems/find-the-distance-value-between-two-arrays/
# Difficulty: Easy
class Solution:
    def findTheDistanceValue(self, arr1, arr2, d):
        c = 0
        for n in arr1:
            if self.isValid(n, arr2, d):
                c += 1
        return c

    def isValid(self, n, arr, d):
        for e in arr:
            if abs(e - n) <= d:
                return False
        return True
