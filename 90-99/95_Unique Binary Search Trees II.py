# -*- coding:utf-8 -*-
# https://leetcode.com/problems/unique-binary-search-trees-ii/description/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n < 1:
            return []
        
        if n == 1:
            return [TreeNode(1)]
        
        trees = self.generateTrees(n - 1)
        
        def copy_tree(root):
            if not root:
                return None
            node = TreeNode(root.val)
            if root.left:
                node.left = copy_tree(root.left)
            if root.right:
                node.right = copy_tree(root.right)
            return node
        
        ret = []
        for tree in trees:
            rp, rc = None, tree
            rc = tree
            while rc:
                node = TreeNode(n)
                if rp is None:
                    node.left = rc
                    ret.append(node)
                else:
                    node.left = rc
                    rp.right = node
                    ret.append(copy_tree(tree))
                    rp.right = rc
                rp, rc = rc, rc.right
                
            rp.right = TreeNode(n)
            ret.append(copy_tree(tree))
            rp.right = None
        
        return ret