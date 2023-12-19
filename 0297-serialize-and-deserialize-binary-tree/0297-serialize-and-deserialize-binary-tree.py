# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        def dfs(root):
            if not root:
                res.append("x")
                return
            
            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        print(res)
        return ' '.join(res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        #format -> root left right leftleft leftright rightleft rightright
        
        def dfs(nodes):
            val = next(nodes)
            if val is 'x':
                return
            curr = TreeNode(val)
            curr.left = dfs(nodes)
            curr.right = dfs(nodes)
            
            return curr
        
        return dfs(iter(data.split()))
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))