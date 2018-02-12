# -*- coding:utf-8 -*-
#https://leetcode.com/problems/valid-sudoku/description/
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row_dict = [{} for i in range(9)]
        col_dict = [{} for i in range(9)]
        cell_dict = [{} for i in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    field, row, col, cell = board[i][j], i, j, i / 3 * 3 + j / 3
                    if (field in row_dict[row]) or (field in col_dict[col]) or (field in cell_dict[cell]):
                        return False
                    row_dict[row][field] = True
                    col_dict[col][field] = True
                    cell_dict[cell][field] = True
        return True