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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        int cnt = 0;
        ListNode *temp = head;
        
        while(temp!=NULL){
            cnt++;
            temp=temp->next;
        }
        
        cnt = cnt-n;
        
        if(cnt==0){
            ListNode *newNode = new ListNode();
            newNode->next=head->next;
            return newNode->next;
        }
        
        temp = head;
        
        while(cnt>1){
            temp=temp->next;
            cnt--;
        }
        
        
        
        temp->next=temp->next->next;
        
        return head;
    }
};