# Problem: 1980. Find Unique Binary String
# LeetCode: https://leetcode.com/problems/find-unique-binary-string/
# Difficulty: Medium

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        def generate(curr):
            if len(curr) == n:
                if curr not in nums:
                    return curr
                
                return ""
            
            add_zero = generate(curr + "0")
            if add_zero:
                return add_zero

            return generate(curr + "1")

        n = len(nums)
        nums = set(nums)
        return generate("")
