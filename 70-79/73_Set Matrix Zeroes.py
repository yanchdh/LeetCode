# -*- coding:utf-8 -*-
# https://leetcode.com/problems/set-matrix-zeroes/description/

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return matrix
        
        row_set, col_set = set(), set()
        
        for i, row in enumerate(matrix):
            for j, val in enumerate(row):
                if val == 0:
                    row_set.add(i)
                    col_set.add(j)
        
        for i in range(len(matrix)):
            for col in col_set:
                matrix[i][col] = 0
        
        for i in range(len(matrix[0])):
            for row in row_set:
                matrix[row][i] = 0