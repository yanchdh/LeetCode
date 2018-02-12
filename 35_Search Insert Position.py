# -*- coding:utf-8 -*-
#https://leetcode.com/problems/search-insert-position/description/
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ret = len(nums)
        l, r = 0, ret - 1
        while l <= r:
            m = l + (r - l) / 2
            if nums[m] >= target:
                ret = m
                r = m - 1
            else:
                l = m + 1
        return ret