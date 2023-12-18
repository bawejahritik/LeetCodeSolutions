# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSameTree(p, q):
            if not p and not q:
                return True
            
            if not p or not q or p.val!=q.val:
                return False
            
            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
        
        
        q = deque([root])
        
        while len(q)>0:
            curr = q.popleft()
            
            if isSameTree(curr, subRoot):
                return True
            
            for child in [curr.left, curr.right]:
                if child is not None:
                    q.append(child)
        
        return False
            
        
        