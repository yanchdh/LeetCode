# -*- coding:utf-8 -*-
# https://leetcode.com/problems/largest-rectangle-in-histogram/description/

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
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