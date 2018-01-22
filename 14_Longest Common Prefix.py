# -*- coding:utf-8 -*-
#https://leetcode.com/problems/longest-common-prefix/description/
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        minstr = min(strs, key=len)
        for j in range(len(minstr)):
            for i in range(len(strs)):
                if minstr[j] != strs[i][j]:
                    return minstr[:j]
        return minstr