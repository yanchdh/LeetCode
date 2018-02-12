# -*- coding:utf-8 -*-
#https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        ret = []
        if not words:
            return ret
        len_s, len_words, len_word = len(s), len(words), len(words[0])
        dict_word = {}
        for word in words:
            dict_word[word] = dict_word.get(word, 0) + 1
        for i in range(len_word):
            begin, end = i, i
            dict_curr = {}
            while end + len_word <= len_s:
                curr = s[end : end + len_word]
                end += len_word
                if curr not in dict_word:
                    begin = end
                    dict_curr = {}
                else:
                    dict_curr[curr] = dict_curr.get(curr, 0) + 1
                    while dict_curr[curr] > dict_word[curr]:
                        dict_curr[s[begin : begin + len_word]] -= 1
                        begin += len_word
                    if begin + len_words * len_word == end:
                        ret.append(begin)
        return ret
