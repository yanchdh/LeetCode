# -*- coding:utf-8 -*-
#https://leetcode.com/problems/permutations-ii/description/
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ret = []
        ret.append(nums[:])
        while self.nextPermutations(nums):
            ret.append(nums[:])
        return ret
    
    def nextPermutations(self, nums):
        n = len(nums)
        i = n - 1
        while i > 0:
            if nums[i] > nums[i - 1]:
                j = i
                while j + 1 < n and nums[i - 1] < nums[j + 1]:
                    j += 1
                nums[i - 1], nums[j] = nums[j], nums[i - 1]
                nums[i:] = nums[-1:-1-(n-i):-1]
                return True
            i -= 1
        return False