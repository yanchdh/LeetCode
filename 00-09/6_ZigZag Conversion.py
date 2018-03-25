# -*- coding:utf-8 -*-
#https://leetcode.com/problems/zigzag-conversion/description/
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        lens = len(s)
        if lens <= numRows or numRows == 1:
            return s
        n = 2 * numRows - 2
        ret = []
        ret.extend(s[::n])
        for i in range(1, numRows - 1):
            k = n - 2 * i
            for j in range(i, lens, n):
                ret.append(s[j])
                try:
                    ret.append(s[j+k])
                except:
                    break
        ret.extend(s[numRows - 1::n])
        return ''.join(ret)
