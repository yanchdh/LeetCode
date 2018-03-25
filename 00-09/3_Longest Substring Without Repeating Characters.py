# -*- coding:utf-8 -*-
#https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        rlen, l, d = 0, 0, {}
        for i in range(len(s)):
            j = d.get(s[i], -1)
            if j >= l:
                rlen = max(rlen, i - l)
                l = j + 1
            d[s[i]] = i
        return max(rlen, len(s) - l)