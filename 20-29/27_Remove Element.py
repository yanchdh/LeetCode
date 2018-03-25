# -*- coding:utf-8 -*-
#https://leetcode.com/problems/remove-element/description/
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i, j, lenn = 0, 0, len(nums)
        while i < lenn:
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
            i += 1
        return j
            