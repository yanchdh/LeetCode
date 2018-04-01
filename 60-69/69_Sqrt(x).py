# -*- coding:utf-8 -*-
# https://leetcode.com/problems/sqrtx/description/

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        ret = 0
        left, right = 0, x / 2 + 1
        while left <= right:
            mid = (left + right) / 2
            if mid * mid <= x:
                ret = mid
                left = mid + 1
            else:
                right = mid - 1
        return ret