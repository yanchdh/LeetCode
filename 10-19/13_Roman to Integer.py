# -*- coding:utf-8 -*-
#https://leetcode.com/problems/roman-to-integer/description/
class Solution(object):
    roman = [["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"], \
            ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"], \
            ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"], \
            ["", "M", "MM", "MMM"]]
    
    def romanNumber(self, s, j, index):
        if index < 0:
            return 0
        rom = Solution.roman[index]
        for i in range(len(rom) - 1, 0, -1):
            if rom[i] == s[j : j + len(rom[i])]:
                return i * (10 ** index) + self.romanNumber(s, j + len(rom[i]), index - 1)
        return self.romanNumber(s, j, index - 1)
    
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        return self.romanNumber(s, 0, 3)