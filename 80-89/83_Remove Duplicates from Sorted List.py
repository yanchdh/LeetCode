# -*- coding:utf-8 -*-
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        h = head
        while h and h.next:
            if h.next.val == h.val:
                h.next = h.next.next
            else:
                h = h.next
        return head