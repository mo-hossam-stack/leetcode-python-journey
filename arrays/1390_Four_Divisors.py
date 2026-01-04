# Problem: Four Divisors
# LeetCode: https://leetcode.com/problems/four-divisors/
# Difficulty: Medium

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        @cache
        def factors(i):
            sum_ = 1 + i
            count = 2
            for f in range(2, floor(sqrt(i)) + 1):
                comp_f = i // f
                if f * comp_f == i:
                    if f == comp_f: return 0
                    sum_ += f + comp_f
                    count += 2
                
                if count > 4: return 0
            
            return sum_ if count == 4 else 0 
        

        return sum(factors(i) for i in nums)
