/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool helper(TreeNode *a, TreeNode *b){
        if(a == NULL && b == NULL) return true;
        if(a == NULL || b == NULL || a->val != b->val) return false;
        
        return helper(a->left, b->right) && helper(a->right, b->left);
    }
    bool isSymmetric(TreeNode* root) {
        if(root == NULL) return true;
        queue<TreeNode *> q;
        q.push(root->left);
        q.push(root->right);
        
        while(!q.empty()){
            TreeNode *left = q.front();
            q.pop();
            TreeNode *right = q.front();
            q.pop();
            
            if(left == NULL && right == NULL) continue;
            if(left == NULL || right == NULL || left->val != right->val) return false;
            q.push(left->left);
            q.push(right->right);
            q.push(left->right);
            q.push(right->left);
        }
        
        
        //return helper(root->left, root->right);
        return true;
    }
};