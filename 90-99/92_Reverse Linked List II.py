# -*- coding:utf-8 -*-
# https://leetcode.com/problems/reverse-linked-list-ii/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        hm_pre = None
        hm = head
        for i in xrange(m - 1):
            hm_pre = hm
            hm = hm.next
        
        hn = hm
        hn_nxt = hn.next
        for i in xrange(m, n):
            nxt = hn_nxt.next
            hn_nxt.next = hn
            hn = hn_nxt
            hn_nxt = nxt
        
        if hm_pre:
            hm_pre.next = hn
        else:
            head = hn
        hm.next = hn_nxt
        
        return head
                