/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode *head = new ListNode();
        ListNode *temp = head;
        int c = 0;
        
        while(l1 != NULL && l2 != NULL){
            int val = l1->val + l2->val;
            
            if(c == 1){
                val = val + 1;
                c = 0;
            }
            
            if(val >= 10){
                val = val - 10;
                c = 1;
            }
            
            ListNode *curr = new ListNode(val);
            temp->next = curr;
            temp = temp->next;
            l1 = l1->next;
            l2 = l2->next;
            
        }
        
        while(l1 != NULL){
            int val = l1->val;
            
            if(c == 1){
                val += c;
                c = 0;
            }
            
            if(val >= 10){
                val = val - 10;
                c = 1;
            }
            
            ListNode *curr = new ListNode(val);
            temp->next = curr;
            temp = temp->next;
            l1 = l1->next;
            
        }
        
         while(l2 != NULL){
            int val = l2->val;
            
            if(c == 1){
                val += c;
                c = 0;
            }
            
            if(val >= 10){
                val = val - 10;
                c = 1;
            }
            
            ListNode *curr = new ListNode(val);
            temp->next = curr;
            temp = temp->next;
            l2 = l2->next;
            
        }
        
        if(c == 1){
            ListNode *newNode = new ListNode(c);
            temp->next = newNode;
            temp = temp->next;
        }
        
        
        return head->next;
        
    }
};