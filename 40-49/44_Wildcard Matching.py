# -*- coding:utf-8 -*-
#https://leetcode.com/problems/wildcard-matching/description/
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        self.lens, self.lenp = len(s), len(p)
        self.dp = [[0 for i in range(self.lenp + 1)] for j in range(self.lens + 1)]
        return self.match(s, p, 0, 0)
        
    def match(self, s, p, i, j):
        ret = False
        if j == self.lenp:
            ret = (i == self.lens)
        elif i == self.lens:
            ret = (p[j] == '*' and self.match(s, p, i, j + 1))
        elif self.dp[i][j]:
            ret = (self.dp[i][j] == 1)
        elif s[i] == p[j] or p[j] == '?':
            ret = self.match(s, p, i + 1, j + 1)
        elif p[j] == '*':
            ret = (self.match(s, p, i + 1, j + 1) or self.match(s, p, i + 1, j) or self.match(s, p, i, j + 1))
        self.dp[i][j] = 1 if ret else -1
        return ret