# -*- coding:utf-8 -*-
# https://leetcode.com/problems/merge-sorted-array/description/

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i1 = m - 1
        i2 = n - 1
        j = m + n - 1
        while i2 >= 0:
            if i1 >= 0 and nums1[i1] > nums2[i2]:
                nums1[j] = nums1[i1]
                i1 -= 1
            else:
                nums1[j] = nums2[i2]
                i2 -= 1
            j -= 1