# -*- coding:utf-8 -*-
# https://leetcode.com/problems/unique-binary-search-trees/description/

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        def f(m):
            if m < 1:
                return {}
            if m == 1:
                return {1: 1}
            tmp_dict = f(m - 1)
            ret_dict = {}
            for k, v in tmp_dict.iteritems():
                for i in range(1, k + 2):
                    ret_dict[i] = ret_dict.get(i, 0) + v
            return ret_dict
        
        return sum(f(n).values())