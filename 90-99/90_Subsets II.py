# -*- coding:utf-8 -*-
# https://leetcode.com/problems/subsets-ii/description/

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1
        
        d_len = len(d)
        d_keys = d.keys()
        ret = []
        
        def f(idx, lst):
            if idx == d_len:
                ret.append(lst[:])
                return
            f(idx + 1, lst)
            lst.append(d_keys[idx])
            f(idx + 1, lst)
            lst.pop()
        
        f(0, [])

        for k, v in d.iteritems():
            if v > 1:
                for i in range(len(ret)):
                    if k not in ret[i]:
                        continue
                    lst = ret[i][:]
                    for j in range(1, v):
                        lst.append(k)
                        ret.append(lst[:])
        return ret