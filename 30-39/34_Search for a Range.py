# -*- coding:utf-8 -*-
#https://leetcode.com/problems/search-for-a-range/description/
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums or nums[-1] < target or target < nums[0]:
            return [-1, -1]
        l = self.binarySearch(nums, target)
        if l == -1 or nums[l] != target:
            return [-1, -1]
        if nums[-1] == target:
            return [l, len(nums) - 1]
        return [l, self.binarySearch(nums, target + 1) - 1]
        
    def binarySearch(self, nums, target):
        ret = -1
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) / 2
            if nums[m] >= target:
                r = m - 1
                ret = m
            else:
                l = m + 1
        return ret