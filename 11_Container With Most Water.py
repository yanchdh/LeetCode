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
            ret = max(ret, min(height[l], height[r]) * (r - l))
            diff = height[l] - height[r]
            if diff <= 0:
                l += 1
                while l < r and height[l] <= height[l - 1]:
                    l += 1
            if diff >= 0:
                r -= 1
                while l < r and height[r] <= height[r + 1]:
                    r -= 1
        return ret