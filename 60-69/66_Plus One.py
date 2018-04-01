# -*- coding:utf-8 -*-
# https://leetcode.com/problems/plus-one/description/

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if not digits:
            return digits
        digits[-1] += 1
        i = len(digits) - 1
        while i > 0 and digits[i] > 9:
            digits[i-1] += digits[i] / 10
            digits[i] %= 10
            i -= 1
        while digits[0] > 9:
            add = digits[0] / 10
            digits[0] %= 10
            digits.insert(0, add)
        return digits