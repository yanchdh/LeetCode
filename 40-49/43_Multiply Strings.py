# -*- coding:utf-8 -*-
#https://leetcode.com/problems/multiply-strings/description/
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        len1, len2 = len(num1), len(num2)
        num = [0 for i in range(len1 + len2)]
        for i in range(len1):
            for j in range(len2):
                num[len1 - 1 - i + len2 - 1 - j] += int(num1[i]) * int(num2[j])
                
        for i in range(len1 + len2 - 1):
            if num[i] > 9:
                num[i + 1] += num[i] / 10
                num[i] %= 10
                
        while num and num[-1] == 0:
            num.pop()
            
        if not num:
            return "0"
        
        return ''.join(map(str, num[::-1]))