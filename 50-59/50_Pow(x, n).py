# -*- coding:utf-8 -*-
#https://leetcode.com/problems/powx-n/description/
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        ret = 1.0
        if n < 0:
            x, n = 1.0 / x, -n
        while n:
            if n & 1:
                ret *= x
            x *= x
            n >>= 1
        return ret