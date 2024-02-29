# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        
        def bfs(root):
            q = deque([root])
            lvl = 0
            while q:
                curr_lvl = []
                for _ in range(len(q)):
                    node = q.popleft()
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                    
                    curr_lvl.append(node.val)
                
                if lvl % 2 == 0:
                    for i in range(len(curr_lvl) -1):
                        if curr_lvl[i] >= curr_lvl[i+1]:
                            return False
                    for i in range(len(curr_lvl)):
                        if curr_lvl[i] % 2 == 0:
                            return False
                else:
                    for i in range(len(curr_lvl) -1):
                        if curr_lvl[i] <= curr_lvl[i+1]:
                            return False
                    for i in range(len(curr_lvl)):
                        if curr_lvl[i] % 2 == 1:
                            return False
                
                lvl += 1
            return True
        
        return bfs(root)