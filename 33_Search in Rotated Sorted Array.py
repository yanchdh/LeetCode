# -*- coding:utf-8 -*-
#https://leetcode.com/problems/search-in-rotated-sorted-array/description/
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.binarySearch(nums, target, 0, len(nums) - 1)
    
    def binarySearch(self, nums, target, l, r):
        if l > r:
            return -1
        m = (l + r) / 2
        if nums[m] == target:
            return m
        if nums[l] <= nums[m]:
            if nums[l] <= target and target <= nums[m]:
                return self.binarySearch(nums, target, l, m - 1)
            else:
                return self.binarySearch(nums, target, m + 1, r)
        else:
            if nums[m] <= target and target <= nums[r]:
                return self.binarySearch(nums, target, m + 1, r)
            else:
                return self.binarySearch(nums, target, l, m - 1)