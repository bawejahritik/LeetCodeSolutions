# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = deque([root])
        
        if not root:
            return res
        
        while len(q) > 0:
            n = len(q)
            curr_lvl = []
            
            for _ in range(n):
                node = q.popleft()
                curr_lvl.append(node.val)
                
                for child in [node.left, node.right]:
                    if child is not None:
                        q.append(child)
            
            res.append(curr_lvl)
        
        return res