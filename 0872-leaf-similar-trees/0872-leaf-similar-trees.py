# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        res = []
        
        def dfs(root):
            if not root:
                return 
            
            if root.left == None and root.right == None:
                res.append(root.val)
                # print(root.val)
            
            dfs(root.left)
            dfs(root.right)
    
        
        dfs(root1)
        l1 = res
        
        res = []
        dfs(root2)
        l2 = res
        
        return l1 == l2