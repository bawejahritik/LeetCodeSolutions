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
        ListNode *head = NULL;
        ListNode *temp = NULL;
        int carry = 0;
        int val = 0;
        
        while(l1 != NULL && l2 != NULL){
            if(l1->val + l2->val + carry > 9){
                val = l1->val + l2->val + carry - 10;
                carry = 1;
            }else{
                val = l1->val + l2->val + carry;
                carry = 0;
            }
            
            if(head == NULL){
                head = new ListNode(val);
                temp = head;
            }else{
                ListNode *newNode = new ListNode(val);
                temp->next = newNode;
                temp = temp->next;
            }
            
            l1 = l1->next;
            l2 = l2->next;
        }
        
        while(l1 != NULL){
            if(l1->val + carry > 9){
                val = l1->val + carry - 10;
                carry = 1;
            }else{
                val = l1->val + carry;
                carry = 0;
            }
            
            ListNode *newNode = new ListNode(val);
            temp->next = newNode;
            temp = temp->next;
            l1 = l1->next;
        }
        
        while(l2 != NULL){
            if(l2->val + carry > 9){
                val = l2->val + carry - 10;
                carry = 1;
            }else{
                val = l2->val + carry;
                carry = 0;
            }
            
            ListNode *newNode = new ListNode(val);
            temp->next = newNode;
            temp = temp->next;
            l2 = l2->next;
        }
        
        if(carry == 1){
            ListNode *newNode = new ListNode(1);
            temp->next = newNode;
            temp = temp->next;
        }
        
        return head;
    }
};