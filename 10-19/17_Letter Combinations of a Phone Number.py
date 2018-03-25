# -*- coding:utf-8 -*-
#https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
class Solution(object):
    digit2letters = { \
            '1': "", '2': "abc", '3': "def", \
            '4': "ghi", '5': "jkl", '6': "mno", \
            '7': "pqrs", '8': "tuv", '9': "wxyz", \
            '*': "", '0': "", '#': "" \
        }
    
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        :algorithm: dfs
        """
        return self.combination(digits, 0, [])
    
    def combination(self, digits, i, ret):
        if i >= len(digits):
            return ret
        letters = Solution.digit2letters.get(digits[i], "")
        if not letters:
            return []
        if not ret:
            ret = list(letters)
        else:
            ret = [v1 + v2 for v1 in ret for v2 in letters]
        return self.combination(digits, i + 1, ret)
