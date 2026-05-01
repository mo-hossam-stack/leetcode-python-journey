# Problem: 2033. Minimum Operations to Make a Uni-Value Grid
# LeetCode: https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid/
# Difficulty: Medium
class Solution:
    def minOperations(self, grid, x):
        nums_array = []
        result = 0

        for row in grid:
            for num in row:
                nums_array.append(num)

        nums_array.sort()

        length = len(nums_array)
        final_common_number = nums_array[length // 2]

        for number in nums_array:
            if number % x != final_common_number % x:
                return -1
            result += abs(final_common_number - number) // x

        return result
