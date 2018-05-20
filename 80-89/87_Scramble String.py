# -*- coding:utf-8 -*-
# https://leetcode.com/problems/scramble-string/description/

class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) != len(s2):
            return False
        if cmp(s1, s2) == 0:
            return True
        l1, l2 = list(s1), list(s2)
        l1.sort()
        l2.sort()
        if cmp(l1, l2) != 0:
            return False
        for S2 in (s2, s2[::-1]):
            for i in xrange(len(s1)):
                if s1[i] == S2[0]:
                    if self.isScramble(s1[:i], S2[1:i+1]) and self.isScramble(s1[i+1:], S2[i+1:]):
                        return True
                    if self.isScramble(s1[i+1:], S2[1:-i]) and self.isScramble(s1[:i], S2[-i:]):
                        return True
        return False