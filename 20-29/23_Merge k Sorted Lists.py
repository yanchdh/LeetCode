# -*- coding:utf-8 -*-
#https://leetcode.com/problems/merge-k-sorted-lists/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from Queue import PriorityQueue

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = ret = ListNode(-1)
        q = PriorityQueue()
        for node in lists:
            if node:
                q.put((node.val, node))
        while not q.empty():
            val, node = q.get()
            head.next = node
            head = head.next
            node = node.next
            if node:
                q.put((node.val, node))
        return ret.next