# -*- coding:utf-8 -*-
# https://leetcode.com/problems/simplify-path/description/

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path_list = path.split('/')
        count = 0
        ret = []
        while path_list:
            name = path_list.pop()
            if name in ['', '.']:
                continue
            if name == '..':
                count += 1
            else:
                if count > 0:
                    count -= 1
                else:
                    ret.append(name)
                    ret.append('/')
        if not ret:
            ret.append('/')
        return ''.join(ret[::-1])