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
    ListNode *reverseList(ListNode *head){
        if(head == NULL || head->next == NULL) return head;
        
        ListNode *prev = NULL;
        ListNode *after = NULL;
        
        while(head!=NULL){
            after=head->next;
            head->next = prev;
            prev = head;
            head=after;
            
        }
        
        //head->next = prev;
        
        return prev;
    }
    bool isPalindrome(ListNode* head) {
        if(head == NULL || head->next == NULL)return true;
    
        ListNode *slow = head;
        ListNode *fast = head;
        
        while(fast->next!= NULL && fast->next->next!=NULL){
            slow = slow->next;
            fast=fast->next->next;
        }
        
        
        slow->next = reverseList(slow->next);
        slow=slow->next;
        fast = head;
        
        while(slow){
           if(slow->val != fast->val) return false;
            
            slow = slow->next;
            fast = fast->next;
        }
        
        return true;
    }
};