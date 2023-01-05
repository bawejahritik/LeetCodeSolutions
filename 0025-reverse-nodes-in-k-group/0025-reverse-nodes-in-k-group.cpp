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
    ListNode* reverseKGroup(ListNode* head, int k) {
        
        ListNode *dummy = new ListNode(0);
        dummy -> next = head;
        
        ListNode *temp = head , *prev = dummy, *after = dummy;
        int c = 0;
        
        while(temp != NULL){
            temp = temp->next;
            c++;
        }
        
        while(c >= k){
            temp = prev->next;
            after = temp->next;
            
            for(int i=1; i<k; i++){
                temp->next = after->next;
                after->next = prev->next;
                prev->next = after;
                after = temp->next;
            }
            
            prev = temp;
            
            c -= k;
        }
        
        return dummy->next;
        

        
    }
};