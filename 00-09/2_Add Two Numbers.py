# -*- coding:utf-8 -*-
#https://leetcode.com/problems/add-two-numbers/description/
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ret = ListNode(-1)
        l = ret
        left = 0
        while (l1 or l2):
            if l1:
                left = left + l1.val
                l1 = l1.next
            if l2:
                left = left + l2.val
                l2 = l2.next
            l.next = ListNode(left % 10)
            l = l.next
            left = left / 10
        if left:
            l.next = ListNode(left)
        return ret.next