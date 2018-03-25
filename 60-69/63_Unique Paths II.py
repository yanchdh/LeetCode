# -*- coding:utf-8 -*-
# https://leetcode.com/problems/unique-paths-ii/description/

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid or not obstacleGrid[0]:
            return 
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[0][0] or obstacleGrid[-1][-1]:
            return 0
        dp = [[0] * (n + 1) for i in range(m + 1)]
        dp[1][1] = 1
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if not obstacleGrid[i-1][j-1]:
                    dp[i][j] += dp[i][j-1] + dp[i-1][j]
        return dp[m][n]