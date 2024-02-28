# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:

        res = [0]
        def bfs(root):
            if not root:
                return -1
            
            q = deque([root])
            curr_len = 0
            
            while q:
                n = len(q)
                new_lvl = []
                for _ in range(n):
                    node = q.popleft()
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                    new_lvl.append(node.val)
                res[0] = new_lvl
        
        bfs(root)
        
        return res[0][0]