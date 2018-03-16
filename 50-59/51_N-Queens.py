# -*- coding:utf-8 -*-
#https://leetcode.com/problems/n-queens/description/
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        ret = []
        def DFS(c, nqueens, flag):
            if c == n:
                ret.append([''.join(nqueens[i]) for i in range(n)])
                return
            for r in range(n):
                if flag[r] or flag[n + r + c] or flag[4 * n - (r - c)]:
                    continue
                flag[r] = flag[n + r + c] = flag[4 * n - (r - c)] = True
                nqueens[r][c] = 'Q'
                DFS(c + 1, nqueens, flag)
                nqueens[r][c] = '.'
                flag[r] = flag[n + r + c] = flag[4 * n - (r - c)] = False
                
        DFS(0, [['.' for j in range(n)] for i in range(n)], [False for i in range(5 * n)])
        return ret