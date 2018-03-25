# -*- coding:utf-8 -*-
# https://leetcode.com/problems/insert-interval/description/

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        ret = []
        for i, interval in enumerate(intervals):
            if interval.start >= newInterval.start and newInterval.end >= interval.end:
                continue
            ap = True
            if interval.start <= newInterval.start <= interval.end:
                newInterval.start = interval.start
                ap = False
            if interval.start <= newInterval.end <= interval.end:
                newInterval.end = interval.end
                ap = False
            if ap:
                ret.append(interval)
        ret.append(newInterval)
        ret.sort(key=lambda x: x.start)
        return ret