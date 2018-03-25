# -*- coding:utf-8 -*-
#https://leetcode.com/problems/longest-palindromic-substring/description/
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        L, R, i, lens = 0, 0, 0, len(s)
        while i < lens:
            l, r = i, i
            while r + 1 < lens:
                if s[r] == s[r+1]:
                    r += 1
                else:
                    break
            i = r + 1
            while l > 0 and r + 1 < lens:
                if s[l - 1] == s[r + 1]:
                    l, r = l - 1, r + 1
                else:
                    break
            if r - l > R - L:
                L, R = l, r
        return s[L:R+1]