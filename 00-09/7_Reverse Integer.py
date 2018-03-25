# -*- coding:utf-8 -*-
#https://leetcode.com/problems/reverse-integer/description/
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 0:
            x = int(str(x)[::-1])
            return (x if x < 0x80000000 else 0)
        else:
            x = int(str(-x)[::-1])
            return (-x if x <= 0x80000000 else 0)