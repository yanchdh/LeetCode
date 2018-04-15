# -*- coding:utf-8 -*-
# https://leetcode.com/problems/word-search/description/

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not word or not board:
            return True
        h = len(board)
        w = len(board[0])
        DIR = [(0,1),(1,0),(-1,0),(0,-1)]
        len_word = len(word)
        
        def search(i, j, idx):
            if idx == len_word:
                return True
            for x, y in DIR:
                _i, _j = i + x, j + y
                if _i < 0 or _i >= h or _j < 0 or _j >= w or board[_i][_j] != word[idx]:
                    continue
                old, board[_i][_j] = board[_i][_j], None
                if search(_i, _j, idx + 1):
                    return True
                board[_i][_j] = old
            return False
       
        for i in xrange(h):
            for j in xrange(w):
                if board[i][j] == word[0]:
                    old, board[i][j] = board[i][j], None
                    if search(i, j, 1):
                        return True
                    board[i][j] = old
        
        return False