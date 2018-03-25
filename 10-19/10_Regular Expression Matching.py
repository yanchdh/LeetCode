# -*- coding:utf-8 -*-
#https://leetcode.com/problems/regular-expression-matching/description/
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        self.ls, self.lp = len(s), len(p)
        self.dp = [[-1 for i in range(self.lp + 1)] for j in range(self.ls + 1)]
        return self.Match(s, p, 0, 0) == 1
    
    def Match(self, s, p, i, j):
        if j == self.lp:
            return 1 if i == self.ls else 0
        
        if self.dp[i][j] != -1:
            return self.dp[i][j]
        
        ret = 0
        if p[j] == '.' and j + 1 < self.lp and p[j + 1] == '*':
            for k in range(i, self.ls + 1):
                if self.Match(s, p, k, j + 2): 
                    ret = 1
                    break
        elif j + 1 < self.lp and p[j + 1] == '*':
            if self.Match(s, p, i, j + 2) or (i < self.ls and s[i] == p[j] and self.Match(s, p, i + 1, j + 1)):
                ret = 1
        elif p[j] == '*':
            if self.Match(s, p, i, j + 1) or (j > 0 and i < self.ls and s[i] == p[j - 1] and (self.Match(s, p, i + 1, j) or self.Match(s, p, i + 1, j + 1))):
                ret = 1
        elif i < self.ls and (p[j] == '.' or s[i] == p[j]):
            if self.Match(s, p, i + 1, j + 1):
                ret = 1
        self.dp[i][j] = ret
        return ret
