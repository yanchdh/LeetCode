# -*- coding:utf-8 -*-
#https://leetcode.com/problems/divide-two-integers/description/
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        ret, sign = 0, 1
        if dividend < 0:
            dividend, sign = -dividend, -sign
        if divisor < 0:
            divisor, sign = -divisor, -sign
        while dividend >= divisor:
            t, n = 1, divisor
            while dividend >= n:
                dividend -= n
                n += n
                ret += t
                t += t
        if ret > 0x7FFFFFFF:
            ret = 0x7FFFFFFF if sign == 1 else 0x7FFFFFFF + 1
        return ret if sign == 1 else -ret