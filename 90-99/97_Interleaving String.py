# -*- coding:utf-8 -*-
# https://leetcode.com/problems/interleaving-string/description/

class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        l1, l2, l3 = len(s1), len(s2), len(s3)
        if l1 + l2 != l3:
            return False
        dp = {}
        
        def f(i, j):
            if i == l1 and j == l2:
                return True
            if (i, j) in dp:
                return dp[(i, j)]
            dp[(i, j)] = (i < l1 and s1[i] == s3[i + j] and f(i + 1, j)) or (j < l2 and s2[j] == s3[i + j] and f(i, j + 1))
            return dp[(i, j)]
        
        return f(0, 0)