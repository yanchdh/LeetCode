# -*- coding:utf-8 -*-
#https://leetcode.com/problems/count-and-say/description/
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        ret = "1"
        for i in range(n - 1):
            tmp, cnt = "", 1
            j, lenr = 1, len(ret)
            while j < lenr:
                if ret[j] == ret[j - 1]:
                    cnt += 1
                else:
                    tmp, cnt = tmp + str(cnt) + ret[j - 1], 1
                j += 1
            ret = tmp + str(cnt) + ret[j - 1]
        return ret