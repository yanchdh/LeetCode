# -*- coding:utf-8 -*-
# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/

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
        ret = ListNode(None)
        ret.next = head
        h = ret
        while h and h.next and h.next.next:
            hnn = h.next.next
            if hnn.val == h.next.val:
                while hnn and hnn.val == h.next.val:
                    hnn = hnn.next
                h.next = hnn
            else:
                h = h.next
        return ret.next