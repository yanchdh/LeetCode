# -*- coding:utf-8 -*-
# https://leetcode.com/problems/sort-colors/description/

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        color_count = [0, 0, 0]
        for color in nums:
            color_count[color] += 1
        idx = 0
        for color, count in enumerate(color_count):
            for _ in xrange(count):
                nums[idx] = color
                idx += 1