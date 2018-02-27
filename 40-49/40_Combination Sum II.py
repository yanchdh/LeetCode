# -*- coding:utf-8 -*-
#https://leetcode.com/problems/combination-sum-ii/description/
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        dp = [[] for i in range(target + 1)]
        dp[0].append([])
        for w in candidates:
            for j in range(target, w - 1, -1):
                for l in dp[j - w]:
                    c = l[:]
                    c.append(w)
                    if c not in dp[j]:
                        dp[j].append(c)
        return dp[target]