# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            if not root:
                return
            
            if root.left is None and root.right is None:
                res.append(root.val)
                return
            
            dfs(root.left)
            dfs(root.right)
            
        
        res = []
        dfs(root1)
        lvs1 = res
        res = []
        dfs(root2)
        lvs2 = res
        print(lvs1, lvs2)
        
        return lvs1==lvs2