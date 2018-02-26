# -*- coding:utf-8 -*-
#https://leetcode.com/problems/combination-sum/description/
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        dp = [[] for i in range(target + 1)]
        dp[0].append(0)
        candidates.sort()
        for w in candidates:
            for j in range(w, target + 1):
                if len(dp[j - w]):
                    dp[j].append(j - w)
        dct = {0 : [[]]}
        return self.dfs(target, dp, dct)
    
    def dfs(self, target, dp, dct):
        ret = dct.get(target)
        if ret is not None:
            return ret
        ret = []
        for i in dp[target]:
            tmp = self.dfs(i, dp, dct)
            for l in tmp:
                if not l or target - i >= l[-1]:
                    ret.append(l[:])
                    ret[-1].append(target - i)
        dct[target] = ret
        return ret