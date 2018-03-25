# -*- coding:utf-8 -*-
#https://leetcode.com/problems/integer-to-roman/description/
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman = [["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"], \
                ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"], \
                ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"], \
                ["", "M", "MM", "MMM"]]
        return roman[3][num / 1000] + roman[2][(num / 100) % 10] + roman[1][(num / 10) % 10] + roman[0][num % 10]