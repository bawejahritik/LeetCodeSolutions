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
    ListNode* removeElements(ListNode* head, int val) {
        if(head == NULL) return head;
        
        
        ListNode *prev = new ListNode;
        prev->next = head;
        ListNode *temp = prev;
        
        while(temp->next != NULL){
            if(temp->next->val == val){
                temp->next = temp->next->next;
                //prev->next = temp->next;
            }else{
               temp = temp->next; 
            }
            
        }
        // if(temp->val = val){
        //     prev->next = NULL;
        // }
        
        return prev->next;
    }
};