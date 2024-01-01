class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if not s or not g:
            return 0
        
        g.sort()
        s.sort()
        
        res = 0
        i, j = 0, 0
        
        while i < len(g) and j < len(s):
            if g[i]<=s[j]:
                res += 1
                j += 1 
                i += 1
            else:
                j += 1
                
        
        return res