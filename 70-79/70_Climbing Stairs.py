# -*- coding:utf-8 -*-
# https://leetcode.com/problems/climbing-stairs/description/

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        pre, cur = 1, 2
        for i in range(3, n + 1):
            pre, cur = cur, pre + cur
        return cur