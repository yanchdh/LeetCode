# -*- coding:utf-8 -*-
#https://leetcode.com/problems/generate-parentheses/description/
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.ret = []
        self.dfs(n, 0, 0, '')
        return self.ret
        
    def dfs(self, n, l, r, s):
        if n * 2 == l + r:
            self.ret.append(s)
            return
        if l == r:
            self.dfs(n, l + 1, r, s + '(')
        else:
            if l < n:
                self.dfs(n, l + 1, r, s + '(')
            self.dfs(n, l, r + 1, s + ')')