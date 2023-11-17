class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        stack = []
        
        def generator(o, c, s, n):
            if o == c == n:
                stack.append(s)
                
            if o<n:
                generator(o+1, c, s+"(", n)             
                
            if c<o:
                generator(o, c+1, s+")", n)
                
        generator(0, 0, "", n)
        
        return stack