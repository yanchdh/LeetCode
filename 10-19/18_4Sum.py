# -*- coding:utf-8 -*-
#https://leetcode.com/problems/4sum/description/
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        ret, lenn = [], len(nums)
        for i in range(lenn - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            #优化
            if sum(nums[i:i+4]) > target or nums[i] + sum(nums[lenn-3:lenn]) < target:
                continue
            for j in range(i + 1, lenn - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                #优化
                if nums[i] + sum(nums[j:j+3]) > target or nums[i] + nums[j] + sum(nums[lenn-2:lenn]) < target:
                    continue
                tmp = nums[i] + nums[j] - target
                l, r = j + 1, lenn - 1
                while l < r:
                    val = tmp + nums[l] + nums[r]
                    if val == 0:
                        ret.append([nums[i], nums[j], nums[l], nums[r]])
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