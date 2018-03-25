# -*- coding:utf-8 -*-
#https://leetcode.com/problems/two-sum/description/
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for j in range(len(nums)):
            i = d.get(nums[j])
            if (i is not None):
                return [i, j]
            d[target - nums[j]] = j
        return [-1, -1]
