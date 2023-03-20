/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* next;

    Node() : val(0), left(NULL), right(NULL), next(NULL) {}

    Node(int _val) : val(_val), left(NULL), right(NULL), next(NULL) {}

    Node(int _val, Node* _left, Node* _right, Node* _next)
        : val(_val), left(_left), right(_right), next(_next) {}
};
*/

class Solution {
public:
    Node* connect(Node* root) {
        if(!root) return root;
        
        queue<Node*> q;
        q.push(root);
        
        while(!q.empty()){
            Node *rightNode = nullptr;
            for(int i=size(q); i; i--){
                auto curr = q.front();
                q.pop();
                curr->next = rightNode;
                rightNode = curr;
                if(curr->right){
                    q.push(curr->right);
                    q.push(curr->left);
                }
            }
        }
        
        return root;
    }
};