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
    vector<int> inorder;
    void getInorder(TreeNode* root){
        if(root == NULL) return;
        
        getInorder(root->left);
        inorder.push_back(root->val);
        getInorder(root->right);
    }
    
    int kthSmallest(TreeNode* root, int k) {
        getInorder(root);
        return inorder[k-1];
    }
};