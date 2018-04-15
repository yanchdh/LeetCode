# -*- coding:utf-8 -*-
# https://leetcode.com/problems/subsets/description/

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        ret = []
        sub = []
        def dfs(idx):
            if idx == n:
                ret.append(sub[:])
                return
            dfs(idx + 1)
            sub.append(nums[idx])
            dfs(idx + 1)
            sub.pop()
        dfs(0)
        return ret