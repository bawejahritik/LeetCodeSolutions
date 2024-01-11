# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        res = [0]
        
        def dfs(root, minYet, maxYet):
            if not root:
                return 
            
            if root.val < minYet:
                minYet = root.val
            
            if root.val > maxYet:
                maxYet = root.val
            
            res[0] = max(res[0], maxYet-minYet)
            
            dfs(root.left, minYet, maxYet)
            dfs(root.right, minYet, maxYet)
        
        dfs(root, float('inf'), 0)
        
        return res[0]