# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxD = [0]
        
        def dfs(root):
            if root is None:
                return -1
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            maxD[0] = max(maxD[0], 2 + left + right)
            return 1+max(left, right) 
        
        dfs(root)
        return maxD[0]