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
    vector<int> temp;
    void inorder(TreeNode *root){
        if(root == NULL) return;
        
        inorder(root->left);
        temp.push_back(root->val);
        inorder(root->right);
    }
    bool findTarget(TreeNode* root, int k) {
        if(root == NULL) return false;
        
        inorder(root);
        
        int i=0, j=temp.size()-1;
        
        while(i<j){
            if(temp[i] + temp[j] == k) return true;
            else if(temp[i] + temp[j] > k) j--;
            else i++;
        }
        
        return false;
    }
};