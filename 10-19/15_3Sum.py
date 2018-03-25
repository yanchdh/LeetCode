# -*- coding:utf-8 -*-
#https://leetcode.com/problems/3sum/description/
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        :algorithm: dp
        """
        nums.sort()
        ret, lenn = [], len(nums)
        for i in range(lenn - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, lenn - 1
            while l < r:
                val = nums[i] + nums[l] + nums[r]
                if val == 0:
                    ret.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                    r -= 1
                    while nums[r] == nums[r + 1] and l < r:
                        r -= 1
                elif val < 0:
                    l += 1
                else:
                    r -= 1
        return ret
