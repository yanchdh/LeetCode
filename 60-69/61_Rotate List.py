# -*- coding:utf-8 -*-
# https://leetcode.com/problems/rotate-list/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None    

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        n, p = 0, head
        while p:
            p = p.next
            n += 1
        
        if n == 0 or k % n == 0:
            return head
        
        k %= n
        left, right = head, head
        while right.next:
            right = right.next
            if k > 0:
                k -= 1
            else:
                left = left.next
        right.next, head, left.next = head, left.next, right.next
        return head