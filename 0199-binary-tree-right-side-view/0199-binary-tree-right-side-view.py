# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        res = []
        q = deque([root])
        
        while len(q)>0:
            n = len(q)
            curr_lvl = []
            
            for _ in range(n):
                node = q.popleft()
                
                for child in [node.left, node.right]:
                    if child:
                        q.append(child)
                
                curr_lvl.append(node)
            
            res.append(curr_lvl[-1].val)
        
        return res