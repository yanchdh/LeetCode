# -*- coding:utf-8 -*-
# https://leetcode.com/problems/length-of-last-word/description/

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret = 0
        pos = len(s) - 1
        while pos >= 0 and s[pos] == ' ':
            pos -= 1
        while pos >= 0 and s[pos] != ' ':
            pos -= 1
            ret += 1
        return ret