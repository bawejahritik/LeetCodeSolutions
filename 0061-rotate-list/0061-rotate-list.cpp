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
    ListNode* rotateRight(ListNode* head, int k) {
        if(head == NULL || k == 0) return head;
        if(head->next == NULL) return head;
        
        ListNode *temp = head;
        ListNode *prev = NULL;
        int c = 0;
        
        while(temp != NULL){
            prev = temp;
            temp=temp->next;
            c++;
        }
        
        prev -> next = head;
        
        if(k > c)k = k%c;
        
        k = c - k;
        
        while(k > 0){
            prev = head;
            head = head->next;
            k--;
        }
        
        prev->next = NULL;
            
        return head;
    }
};