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
        lists = list(s)
        ret.extend(lists[::n])
        for i in range(1, numRows - 1):
            j, k = i, n - 2 * i
            while j < lens:
                ret.append(lists[j])
                j += k
                k = n - k
        ret.extend(lists[numRows - 1::n])
        return ''.join(ret)