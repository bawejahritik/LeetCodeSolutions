# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        res1 = []
        res2 = []
        
        path=[]
        
        def dfs(root):
            if root is None:
                path.append('*')
                return
            
            path.append(root.val)
            
            dfs(root.left)
            dfs(root.right)
            
        
        dfs(p)
        res1 = path
        path = []
        dfs(q)
        res2 = path
        
        print(res1, res2, path)
        
        return res1==res2
                