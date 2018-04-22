# -*- coding:utf-8 -*-
# https://leetcode.com/problems/maximal-rectangle/description/

class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        
        def largestRectangleArea(heights):
            ret = 0
            ascent_heights = []
            ascent_idxs = []
            n = len(heights)
            for idx, height in enumerate(heights):
                if not ascent_heights or ascent_heights[-1] < height:
                    ascent_heights.append(height)
                    ascent_idxs.append(idx)
                elif ascent_heights[-1] > height:
                    while ascent_heights and ascent_heights[-1] > height:
                        _height = ascent_heights.pop()
                        _idx = ascent_idxs.pop()
                        ret = max(ret, _height * (idx - _idx))
                    ascent_heights.append(height)
                    ascent_idxs.append(_idx)
            while ascent_heights:
                ret = max(ret, ascent_heights.pop() * (n - ascent_idxs.pop()))
            return ret
        
        if not matrix:
            return 0
        
        row = len(matrix)
        col = len(matrix[0])
        
        ret = 0
        heights = [0 for i in range(col)]
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0
            ret = max(ret, largestRectangleArea(heights))
        return ret