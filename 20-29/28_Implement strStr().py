# -*- coding:utf-8 -*-
#https://leetcode.com/problems/implement-strstr/description/
class Solution(object):
    """
    :algorithm: kmp
    """
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        fail = self.getFail(needle)
        i, j, lenh, lenn = 0, 0, len(haystack), len(needle)
        while i < lenh:
            while j > 0 and haystack[i] != needle[j]:
                j = fail[j]
            if haystack[i] == needle[j]:
                j += 1
            i += 1
            if j == lenn:
                return i - j
        return -1
    
    def getFail(self, s):
        i, j, lens, fail = 1, 0, len(s), [0, 0]
        while i < lens:
            while j > 0 and s[i] != s[j]:
                j = fail[j]
            if s[i] == s[j]:
                j += 1
            i += 1
            fail.append(j)
        return fail