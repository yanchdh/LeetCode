# -*- coding:utf-8 -*-
#https://leetcode.com/problems/median-of-two-sorted-arrays/description/
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1, len2 = len(nums1), len(nums2)
        if len1 > len2:
            nums1, nums2, len1, len2 = nums2, nums1, len2, len1 
            
        if len2 == 0:
            raise ValueError
            
        halflen = (len1 + len2 + 1) / 2
        minright, maxleft = 0, 0
        
        if len1 == 0:
            if (len1 + len2) % 2 == 0:
                return (float)(nums2[halflen - 1] + nums2[halflen]) / 2
            return nums2[halflen - 1]
        
        l, r = 0, len1
        while l <= r:
            i = (l + r) / 2
            j = halflen - i
            if i < len1 and nums2[j - 1] > nums1[i]:
                l = i + 1
            elif i > 0 and nums1[i - 1] > nums2[j]:
                r = i - 1
            else:
                if i == 0:
                    maxleft = nums2[j - 1]
                elif j == 0:
                    maxleft = nums1[i - 1]
                else:
                    maxleft = max(nums1[i - 1], nums2[j - 1])
                    
                if (len1 + len2) % 2 == 0:
                    if i == len1:
                        minright = nums2[j]
                    elif j == len2:
                        minright = nums1[i]
                    else:
                        minright = min(nums1[i], nums2[j])
                
                if (len1 + len2) % 2 == 0:
                    return (float)(maxleft + minright) / 2
                return maxleft