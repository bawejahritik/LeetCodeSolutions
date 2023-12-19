# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        
        res = [0]
        res[0] = float('-inf')
        
        def helper(root):
            if not root:
                # print(path)
                return 0
            
            leftPath = max(helper(root.left), 0)
            rightPath = max(helper(root.right), 0)
            
            total = root.val + leftPath + rightPath
            
            res[0] = max(res[0], total)

            return root.val + max(leftPath, rightPath)
        
        temp = helper(root)
        
        return res[0]
        
        
        