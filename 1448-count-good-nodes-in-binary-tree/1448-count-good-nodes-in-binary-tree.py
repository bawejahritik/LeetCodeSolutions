# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = [0]
        
        if not root:
            return 0
        
        
        def dfs(root, maxYet):
            if not root:
                return
            
            if root.val >= maxYet:
                ans[0] += 1
                dfs(root.left, root.val)
                dfs(root.right, root.val)
            else:
                dfs(root.left, maxYet)
                dfs(root.right, maxYet)
        
        
        dfs(root, float('-inf'))
        return ans[0]