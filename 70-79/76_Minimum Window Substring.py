# -*- coding:utf-8 -*-
# https://leetcode.com/problems/minimum-window-substring/description/

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        wi, wj = None, None
        ds, dt = {}, {}
        for c in t:
            ds[c], dt[c] = 0, dt.get(c, 0) + 1
        count, i = 0, 0
        for j, c in enumerate(s):
            if c not in dt:
                continue
            ds[c] += 1
            if ds[c] == dt[c]:
                count += 1
            if count < len(dt):
                continue
            while i <= j and ds.get(s[i], 0) > dt.get(s[i], -1):
                if s[i] in ds:
                    ds[s[i]] -= 1
                i += 1
            if wi is None or j - i < wj - wi:
                wi, wj = i, j
            count -= 1
            ds[s[i]] -= 1
            i += 1
        return '' if wi is None else s[wi:wj+1]