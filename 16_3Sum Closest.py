# -*- coding:utf-8 -*-
#https://leetcode.com/problems/3sum-closest/description/
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        ret, lenn = sum(nums[:3]), len(nums)
        for i in range(lenn - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, lenn - 1
            while l < r:
                val = nums[i] + nums[l] + nums[r] - target
                if val == 0:
                    return target
                if abs(val) < abs(ret):
                    ret = val
                if val > target:
                    r -= 1
                else:
                    l += 1
        return ret + target