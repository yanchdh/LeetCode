// URL: https://leetcode.com/problems/sum-of-left-leaves/
// Author: liy
// Desc: binary tree, simple
// Date: 2020-03-17

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int sumOfLeftLeaves(TreeNode* root) {
        int sum = 0;
        if (!root) return sum;
        TreeNode *left = root->left, *right = root->right;
        if (left && !left->left && !left->right)
            sum += left->val;
        sum += left ? sumOfLeftLeaves(left) : 0;
        sum += right ? sumOfLeftLeaves(right) : 0;
        return sum;
    }
};