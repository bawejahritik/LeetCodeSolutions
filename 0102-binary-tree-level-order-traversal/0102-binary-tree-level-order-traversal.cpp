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
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> ans;
        if(root == NULL) return {};
        
        queue<TreeNode *> q;
        q.push(root);
        
        while(!q.empty()){
            int l = q.size();
            vector<int> temp;
            for(int i=0; i<l; i++){
                TreeNode *curr = q.front();
                q.pop();
                if(curr){
                    
                 temp.push_back(curr->val);
                q.push(curr->left);
                q.push(curr->right);
                }
            }
            
            if(!temp.empty()) ans.push_back(temp);
            
        }
        
        return ans;
    }
};