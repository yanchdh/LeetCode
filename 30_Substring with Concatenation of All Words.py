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
        ret, lens, lenw = [], len(s), len(words)
        wd, l = {}, [0]
        for word in words:
            l.append(l[-1] + len(word))
            wd[word] = wd.get(word, 0) + 1
        for i in range(lens - l[-1] + 1):
            if s[i+l[0]:i+l[1]] not in wd:
                continue
            copy = wd.copy()
            j = 0
            while j < lenw:
                ss = s[i+l[j]:i+l[j+1]]
                v = copy.get(ss)
                if not v:
                    break
                elif v == 1:
                    copy.pop(ss)
                else:
                    copy[ss] = v - 1
                j += 1
            if not copy:
                ret.append(i)
        return ret