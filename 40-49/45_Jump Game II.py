# -*- coding:utf-8 -*-
#https://leetcode.com/problems/jump-game-ii/description/
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        n = len(nums)
        dp = [0 for i in range(n)]
        j = 0
        for i in range(1, n):
            while j < i:
                if j + nums[j] >= i:
                    dp[i] = dp[j] + 1
                    break
                j += 1
        return dp[n - 1]