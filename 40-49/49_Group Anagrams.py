# -*- coding:utf-8 -*-
#https://leetcode.com/problems/group-anagrams/description/
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ret, dct = [], {}
        for s in strs:
            l = list(s)
            l.sort()
            ss = ''.join(l)
            j = dct.get(ss, -1)
            if j == -1:
                dct[ss] = j = len(ret)
                ret.append([])
            ret[j].append(s)
        return ret