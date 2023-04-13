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
    ListNode* oddEvenList(ListNode* head) {
        if(head == NULL || head->next == NULL || head->next->next == NULL) return head;
        
        ListNode *odd = head;
        ListNode *even = head->next;
        
        while(even &&even->next && even->next->next){
            cout<<"slow "<<odd->val<<" fast "<<even->val<<endl;
            ListNode* temp = odd->next;
            odd->next = even->next;
            even->next = even->next->next;
            odd->next->next = temp;
            
            odd = odd->next;
            even = even->next;
            cout<<"slow after  "<<odd->val<<" fast after "<<even->val<<endl;
            
        }
        
        cout<<"slow "<<odd->val<<" fast "<<even->val;
        ListNode* temp = odd->next;
        cout<<"Temp "<<temp->val<<endl;
        odd->next = even->next;
        if(even->next == NULL){
            odd->next = temp;
            return head;
        }
        even->next = even->next->next;
        odd->next->next = temp;
            
        
        return head;
        
    }
};