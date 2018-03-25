# -*- coding:utf-8 -*-
#https://leetcode.com/problems/swap-nodes-in-pairs/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        ret = head.next
        pre, cur, nxt = None, head, head.next
        while nxt:
            if pre:
                pre.next = nxt
            cur.next, nxt.next = nxt.next, cur
            pre, cur, nxt = cur, cur.next, None
            if cur:
                nxt = cur.next
        return ret
            