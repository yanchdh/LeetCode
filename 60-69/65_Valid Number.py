# -*- coding:utf-8 -*-
# https://leetcode.com/problems/valid-number/description/

class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        SIGN = '+-'
        
        first, last = 0, len(s) - 1
        while first <= last and s[first] == ' ':
            first += 1
            
        while last >= first and s[last] == ' ':
            last -= 1
            
        if first > last:
            return False
        
        if s[first] in SIGN:
            first += 1
        
        if s[first] == 'e' or s[last] == 'e' or s[last] in SIGN:
            return False
        
        point, e = -1, -1
        i = first
        while i <= last:
            if s[i] == 'e':
                if e != -1:
                    return False
                e = i
                if i + 1 <= last and s[i + 1] in SIGN:
                    i += 1
            elif s[i] == '.':
                if point != -1 or e != -1:
                    return False
                point = i
            elif s[i] < '0' or s[i] > '9':
                return False
            i += 1
        
        if point == first and (point + 1 == e or point == last):
            return False
        
        return True