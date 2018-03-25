# -*- coding:utf-8 -*-
#https://leetcode.com/problems/string-to-integer-atoi/description/
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        num, sign = 0, 1
        i, lens = 0, len(str)
        
        while i < lens and str[i] == ' ':
            i += 1
            
        if i < lens and (str[i] == '+' or str[i] == '-'):
            if str[i] == '-':
                sign = -1
            i += 1
        
        while i < lens and str[i] >= '0' and str[i] <= '9':
            i, num = i + 1, num * 10 + int(str[i])
        
        return max(-0x80000000, min(0x7FFFFFFF, sign * num))