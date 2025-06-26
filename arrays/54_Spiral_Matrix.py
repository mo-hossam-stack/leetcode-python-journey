# Problem: Spiral Matrix
# LeetCode: https://leetcode.com/problems/spiral-matrix/description/
# Difficulty: Medium

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        while matrix:
            #Add first row of the matrix
            res+=matrix.pop(0) 
            #append last element of all lists in order
            if matrix and matrix[0]:
                for row in matrix:
                    res.append(row.pop())
            #add reverse of last row
            if matrix:
                res+= (matrix.pop()[::-1])
            #append first element of all row in reversed 
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    res.append(row.pop(0))
        return res