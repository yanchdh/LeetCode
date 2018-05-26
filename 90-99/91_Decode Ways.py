# -*- coding:utf-8 -*-
# https://leetcode.com/problems/decode-ways/description/

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [-1 for i in xrange(len(s))]
        def f(j):
            if j < 0:
                return 1
            if dp[j] >= 0:
                return dp[j]
            _sum = 0
            if s[j] != '0':
                _sum += f(j - 1)
            if j > 0 and '10' <= s[j-1:j+1] <= '26':
                _sum += f(j - 2)
            dp[j] = _sum
            return _sum
        return f(len(s) - 1)