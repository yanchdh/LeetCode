# -*- coding:utf-8 -*-
#https://leetcode.com/problems/trapping-rain-water/description/
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        if n < 2:
            return 0
        ret = 0
        s, j = 0, 0
        for i in range(n):
            if height[i] >= height[j]:
                ret, s, j = ret + s, 0, i
            else:
                s += height[j] - height[i]
        if s > 0:
            s, j, k = 0, n - 1, j
            for i in range(n - 1, k - 1, -1):
                if height[i] >= height[j]:
                    ret, s, j = ret + s, 0, i
                else:
                    s += height[j] - height[i]
        return ret