# -*- coding:utf-8 -*-
# https://leetcode.com/problems/spiral-matrix-ii/description/

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        return self.fill(0, n - 1, 1, [[0] * n for i in range(n)])
    
    def fill(self, x, y, num, matrix):
        if x >= y:
            if x == y:
                matrix[x][y] = num
            return matrix
        
        for i in range(x, y):
            matrix[x][i] = num
            num += 1
            
        for i in range(x, y):
            matrix[i][y] = num
            num += 1
        
        for i in range(y, x, -1):
            matrix[y][i] = num
            num += 1
        
        for i in range(y, x, -1):
            matrix[i][x] = num
            num += 1
        
        return self.fill(x + 1, y - 1, num, matrix)