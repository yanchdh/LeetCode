# -*- coding:utf-8 -*-
#https://leetcode.com/problems/maximum-subarray/description/
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = 0
        s = 0
        for num in nums:
            s += num
            if s < 0:
                s = 0
            elif s > ret:
                ret = s
        return ret if ret > 0 else max(nums)