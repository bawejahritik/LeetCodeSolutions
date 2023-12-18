# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        def checker(root, minLeft, maxRight):
            if not root:
                return True
            
            if minLeft<root.val<maxRight:
                return checker(root.left, minLeft, root.val) and checker(root.right, root.val, maxRight)
            
            return False
        
        return checker(root, float('-inf'), float('inf'))