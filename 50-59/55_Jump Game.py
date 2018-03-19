# -*- coding:utf-8 -*-
# https://leetcode.com/problems/jump-game/description/
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums) - 1
        left = n
        for i in range(n - 1, -1, -1):
            if nums[i] + i >= left:
                left = i
        return left <= 0