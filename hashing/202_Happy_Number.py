# Problem: 202. Happy Number
# LeetCode: https://leetcode.com/problems/happy-number/
# Difficulty: Easy
class Solution:
    def isHappy(self, n: int) -> bool:    
        visit = set()
        
        def get_next_number(n):    
            output = 0
            
            while n:
                digit = n % 10
                output += digit ** 2
                n = n // 10
            
            return output

        while n not in visit:
            visit.add(n)
            n = get_next_number(n)
            if n == 1:
                return True
        
        return False
