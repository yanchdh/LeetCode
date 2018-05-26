# -*- coding:utf-8 -*-
# https://leetcode.com/problems/binary-tree-inorder-traversal/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        
        def f(root):
            if not root:
                return
            root.left and f(root.left)
            ret.append(root.val)
            root.right and f(root.right)
        
        f(root)
        return ret