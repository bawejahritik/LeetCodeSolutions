class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def generator(openCount, closeCount, curr):
            if openCount == closeCount == n:
                res.append(curr)
            
            if openCount < n:
                generator(openCount+1, closeCount, curr+"(")
            
            if closeCount < openCount:
                generator(openCount, closeCount+1, curr + ")")
        
        generator(0, 0, "")
        
        return res
                