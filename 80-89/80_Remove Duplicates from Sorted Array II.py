# -*- coding:utf-8 -*-
# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 2:
            return n
        p, j = nums[0], 2
        for i in xrange(2, n):
            if nums[i] != p:
                nums[j], p = nums[i], nums[i-1]
                j += 1
        return j