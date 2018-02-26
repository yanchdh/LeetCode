# -*- coding:utf-8 -*-
#https://leetcode.com/problems/sudoku-solver/description/
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        N, n = 9, 3
        self.rows = [[False for i in range(N)] for j in range(N)]
        self.cols = [[False for i in range(N)] for j in range(N)]
        self.cells = [[False for i in range(N)] for j in range(N)]
        for i in range(N):
            for j in range(N):
                if board[i][j] != '.':
                    v = int(board[i][j])
                    self.rows[i][v - 1] = True
                    self.cols[j][v - 1] = True
                    self.cells[i / 3 * 3 + j / 3][v - 1] = True
                    
        self.dfs(board, 0, N)
        
    def dfs(self, board, depth, n):
        if depth == n * n:
            return True
        i, j = depth / n, depth % n
        if board[i][j] != '.':
            return self.dfs(board, depth + 1, n)
        k = i / 3 * 3 + j / 3
        for v in range(n):
            if self.rows[i][v] or self.cols[j][v] or self.cells[k][v]:
                continue
            self.rows[i][v] = self.cols[j][v] = self.cells[k][v] = True
            board[i][j] = str(v + 1)
            if self.dfs(board, depth + 1, n):
                return True
            board[i][j] = "."
            self.rows[i][v] = self.cols[j][v] = self.cells[k][v] = False
        return False