# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        temp = head
        stack = []
        
        while temp.next:
            stack.append(temp.next)
            temp = temp.next
        
        temp = head
        i, j = 0, len(stack)-1
        while i<=j:
            temp.next = stack[j]
            temp = temp.next
            temp.next = stack[i]
            temp = temp.next
            i+=1
            j-=1
        
        temp.next = None