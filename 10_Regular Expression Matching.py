# -*- coding:utf-8 -*-
#https://leetcode.com/problems/regular-expression-matching/description/
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        self.s = s
        self.p = p
        self.lens = len(s)
        self.lenp = len(p)
        self.dp = [[-1 for i in range(self.lenp + 1)] for j in range(self.lens + 1)]
        return self.Match(0, 0) == 1
    
    def Match(self, i, j):
        if j == self.lenp:
            return 1 if i == self.lens else 0
        
        if self.dp[i][j] != -1:
            return self.dp[i][j]
        
        ret = 0
        if self.p[j] == '.':
            if j + 1 < self.lenp and self.p[j + 1] == '*':
                for k in range(i, self.lens + 1):
                    if self.Match(k, j + 2):
                        ret = 1
                        break
            else:
                ret = i < self.lens and self.Match(i + 1, j + 1)
        elif self.p[j] == '*':
            if self.Match(i, j + 1) or \
                (j > 0 and i < self.lens and self.s[i] == self.p[j - 1] and (self.Match(i + 1, j) or self.Match(i + 1, j + 1))):
                ret = 1
        elif j + 1 < self.lenp and self.p[j + 1] == '*':
            if self.Match(i, j + 2) or (i < self.lens and self.s[i] == self.p[j] and self.Match(i + 1, j + 1)):
                ret = 1
        else:
            if i < self.lens and self.s[i] == self.p[j] and self.Match(i + 1, j + 1):
                ret = 1
        self.dp[i][j] = ret
        return ret