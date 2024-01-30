# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        prev = None
        curr = head
        after = head.next
        
        while after:
            curr.next = prev
            prev = curr
            curr = after
            after = after.next
        
        curr.next = prev
        prev = curr
        
        return prev
            