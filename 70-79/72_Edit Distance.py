# -*- coding:utf-8 -*-
# https://leetcode.com/problems/edit-distance/description/

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        
        dp = [[-1] * len(word2) for _ in range(len(word1))]
        
        def match(i, j):
            if j == -1 or i == -1:
                return max(i, j) + 1
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            if word1[i] == word2[j]:
                dp[i][j] = match(i - 1, j - 1)
            else:
                dp[i][j] = 1 + min(match(i - 1, j - 1), min(match(i, j - 1), match(i - 1, j)))
            
            return dp[i][j]
        
        return match(len(word1) - 1, len(word2) - 1)