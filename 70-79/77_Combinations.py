# -*- coding:utf-8 -*-
# https://leetcode.com/problems/combinations/description/

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        
        def _combine(n, k):
            if k < 1:
                return [[]]
            if n == k:
                return [range(1, n + 1)]
            if k == 1:
                return [[i] for i in range(1, n + 1)]
            
            ret = _combine(n - 1, k)
            
            for v in _combine(n - 1, k - 1):
                v.append(n)
                ret.append(v)
            
            return ret
        
        return [] if k > n else _combine(n, k)