# -*- coding:utf-8 -*-
# https://leetcode.com/problems/add-binary/description/

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = map(int, a[::-1])
        b = map(int, b[::-1])
        if len(a) < len(b):
            a, b = b, a
        
        len_a, len_b = len(a), len(b)
        
        for i in range(len_a):
            if i < len_b:
                a[i] += b[i]
            if a[i] > 1:
                if i + 1 == len_a:
                    a.append(0)
                a[i + 1] += a[i] / 2
                a[i] %= 2
        
        return ''.join(map(str, a[::-1]))