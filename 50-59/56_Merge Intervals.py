# -*- coding:utf-8 -*-
# https://leetcode.com/problems/merge-intervals/

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort(key=lambda x: x.start)
        
        if len(intervals) < 2:
            return intervals
        
        ret = []
        pre = intervals[0]
        
        for i in range(1, len(intervals)):
            nxt = intervals[i]
            if nxt.end >= pre.end >= nxt.start:
                pre.end = nxt.end
            elif nxt.start > pre.end:
                ret.append(pre)
                pre = nxt
        ret.append(pre)
        
        return ret