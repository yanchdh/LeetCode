# -*- coding:utf-8 -*-
#https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        remove, ret = None, head
        while n > 0 and head:
            n -= 1
            head = head.next
        if not head:
            return ret.next
        remove = ret
        while head.next:
            head, remove = head.next, remove.next
        remove.next = remove.next.next
        return ret