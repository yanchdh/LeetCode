# -*- coding:utf-8 -*-
#https://leetcode.com/problems/n-queens-ii/description/
class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        def DFS(c, flag):
            if c == n:
                return 1
            N = 0
            for r in range(n):
                if flag[r] or flag[n + r + c] or flag[4 * n - (r - c)]:
                    continue
                flag[r] = flag[n + r + c] = flag[4 * n - (r - c)] = True
                N += DFS(c + 1, flag)
                flag[r] = flag[n + r + c] = flag[4 * n - (r - c)] = False
            return N
        
        return DFS(0, [False for i in range(5 * n)])