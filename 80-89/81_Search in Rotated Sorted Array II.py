# -*- coding:utf-8 -*-
# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) >> 1
            if target == nums[m] or target == nums[l] or target == nums[r]:
                return True
            if nums[l] < nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            elif nums[m] < nums[r]:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                l += 1
                r -= 1
        return False