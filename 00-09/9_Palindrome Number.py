# -*- coding:utf-8 -*-
#https://leetcode.com/problems/palindrome-number/description/
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x <= 0:
            return x == 0
        lenx = int(math.log(x, 10)) + 1
        for i in range(lenx / 2):
            if x / (10**i) % 10 != x / (10**(lenx - i - 1)) % 10:
                return False
        return True