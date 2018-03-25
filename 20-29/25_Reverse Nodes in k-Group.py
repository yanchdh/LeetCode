# -*- coding:utf-8 -*-
#https://leetcode.com/problems/reverse-nodes-in-k-group/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k <= 1:
            return head
        ret, pre = None, None
        while head:
            cur, nxt = head, head.next
            lst, n = head, k - 1
            while lst.next and n > 0:
                lst, n = lst.next, n - 1
            if n > 0:
                break
            ret = ret or lst
            if pre:
                pre.next = lst
            pre, head = head, lst.next
            pre.next = head
            while cur != lst:
                cur, nxt.next, nxt = nxt, cur, nxt.next
        return ret or head