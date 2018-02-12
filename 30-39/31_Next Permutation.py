# -*- coding:utf-8 -*-
#https://leetcode.com/problems/next-permutation/description/
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        lenn = len(nums)
        i = lenn - 1
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1
        if i == 0:
            nums[:] = nums[::-1]
            return
        j = lenn - 1
        while j > 0 and nums[i - 1] >= nums[j]:
            j -= 1
        nums[i - 1], nums[j] = nums[j], nums[i - 1]
        nums[i:] = nums[-1:i - 1:-1]
