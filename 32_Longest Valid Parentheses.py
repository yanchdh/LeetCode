# -*- coding:utf-8 -*-
#https://leetcode.com/problems/longest-valid-parentheses/description/
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret, lens = 0, len(s)
        dp = [0 for i in range(lens)]
        for i in range(1, lens):
            if s[i] == ')':
                j = i - 1 if dp[i - 1] == 0 else i - 1 - dp[i - 1]
                if j >= 0 and s[j] == '(':
                    dp[i] = dp[i - 1] + 2
                    if j > 0:
                        dp[i] += dp[j - 1]
                    if dp[i] > ret:
                        ret = dp[i]
        return ret