# -*- coding:utf-8 -*-
# https://leetcode.com/problems/spiral-matrix/description/
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ret = []
        if not matrix or not matrix[0]:
            return ret
        i1, i2 = 0, len(matrix) - 1
        j1, j2 = 0, len(matrix[0]) - 1
        while i1 <= i2 and j1 <= j2:
            if i1 == i2:
                ret.extend(matrix[i1][j1 : j2 + 1])
                break
            if j1 == j2:
                [ret.append(matrix[i][j1]) for i in range(i1, i2 + 1)]
                break
            ret.extend(matrix[i1][j1 : j2])
            [ret.append(matrix[i][j2]) for i in range(i1, i2)]
            ret.extend(matrix[i2][j2 : j1 : -1])
            [ret.append(matrix[i][j1]) for i in range(i2, i1, -1)]
            i1 += 1
            i2 -= 1
            j1 += 1
            j2 -= 1
        return ret