# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        
        startNode = None
        p = defaultdict(lambda: None)
        q = deque([root])
        
        while q:
            node = q.popleft()
            if node.left:
                p[node.left] = node
                q.append(node.left)
            if node.right:
                p[node.right] = node
                q.append(node.right)
            if node.val == start:
                startNode = node
        
        q = deque([startNode])
        visited = set([startNode])
        time = 0
        
        while q:
            n = len(q)
            for _ in range(n):
                curr = q.popleft()
                if curr.left and curr.left not in visited:
                    visited.add(curr.left)
                    q.append(curr.left)
                if curr.right and curr.right not in visited:
                    visited.add(curr.right)
                    q.append(curr.right)
                if p[curr] and p[curr] not in visited:
                    visited.add(p[curr])
                    q.append(p[curr])
            time += 1

        return time-1