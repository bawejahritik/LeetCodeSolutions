# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        
        def dfs(root, targetSum, path):
            if not root:
                return
            
            if root.left is None and root.right is None and targetSum == root.val:
                path.append(root.val)
                res.append(path[:])
                return
            
            dfs(root.left, targetSum-root.val, path + [root.val])
            dfs(root.right, targetSum-root.val, path + [root.val])
            
        dfs(root, targetSum, [])
        
        return res