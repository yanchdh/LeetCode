# -*- coding:utf-8 -*-
# https://leetcode.com/problems/gray-code/description/

class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n <= 0:
            return [0]
        ret = [0, 1]
        for i in xrange(1, n):
            m = len(ret)
            for j in xrange(m - 1, -1, -1):
                ret.append(m + ret[j])
        return ret
        