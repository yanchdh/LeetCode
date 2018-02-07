# -*- coding:utf-8 -*-
#https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not words:
            return []
        ret, lens, lenword, lenwords = [], len(s), len(words[0]), len(words)
        wd, wl = {}, []
        for word in words:
            j = wd.get(word)
            if j is None:
                wd[word] = len(wl)
                wl.append(1)
            else:
                wl[j] += 1
        
        sl, il, nl = [], [], [0 for i in range(lenword)]
        for i in range(lens - lenword + 1):
            sl.append(wd.get(s[i : i + lenword]))
            if sl[-1] is not None:
                nl[i % lenword] += 1
                if nl[i % lenword] >= lenwords:
                    il.append(i - lenword * (lenwords - 1))
            else:
                nl[i % lenword] = 0
        
        for i in il:
            j, k = i, i + lenword * lenwords
            copy = wl[:]
            while j < k and copy[sl[j]]:
                copy[sl[j]] -= 1
                j += lenword
            if j >= k:
                ret.append(i)
        return ret
