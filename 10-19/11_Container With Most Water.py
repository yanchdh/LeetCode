# -*- coding:utf-8 -*-
#https://leetcode.com/problems/container-with-most-water/description/
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height) - 1
        ret = 0
        while l < r:
            if height[l] < height[r]:
                ret = max(ret, height[l] * (r - l))
                l += 1
            else:
                ret = max(ret, height[r] * (r - l))
                r -= 1
        return ret