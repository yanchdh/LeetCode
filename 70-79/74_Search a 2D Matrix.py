# -*- coding:utf-8 -*-
# https://leetcode.com/problems/search-a-2d-matrix/description/

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        rows, cols = len(matrix), len(matrix[0])
        l, r = 0, rows - 1
        row, col = None, None
        while l <= r:
            m = (l + r) >> 1
            if matrix[m][-1] >= target:
                r = m - 1
                row = m
            else:
                l = m + 1
        if row is None:
            return False
        l, r = 0, cols - 1
        while l <= r:
            m = (l + r) >> 1
            if matrix[row][m] >= target:
                r = m - 1
                col = m
            else:
                l = m + 1
        return False if col is None else matrix[row][col] == target