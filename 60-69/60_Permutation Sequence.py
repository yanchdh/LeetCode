# -*- coding:utf-8 -*-
# https://leetcode.com/problems/permutation-sequence/description/

class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        factorial = [1]
        for i in range(1, n):
            factorial.append(i * factorial[-1])
        num = [i for i in range(1, n + 1)]
        ret = []
        for i in range(n - 1, -1, -1):
            m = factorial[i]
            ret.append(num.pop((k - 1) / m))
            k = ((k - 1) % m) + 1
        return ''.join(map(str, ret))