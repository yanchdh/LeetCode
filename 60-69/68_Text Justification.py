# -*- coding:utf-8 -*-
# https://leetcode.com/problems/text-justification/description/

class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        def convert(line, space, is_last=False):
            new_line = []
            interval = len(line) - 1
            for word in line:
                if is_last:
                    count = 1 if interval > 0 else space
                else:
                    count = (space + interval - 1) / interval if interval > 0 else space
                space -= count
                interval -= 1
                new_line.append(word)
                new_line.append(' ' * count)
            return ''.join(new_line)
        
        ret = []
        line, width = [], 0
        for word in words:
            if width + len(line) + len(word) > maxWidth:
                ret.append(convert(line, maxWidth - width))
                line, width = [], 0
            line.append(word)
            width += len(word)
        ret.append(convert(line, maxWidth - width, True))
        return ret