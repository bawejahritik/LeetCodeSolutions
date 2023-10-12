class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openB = "({["
        closeB = ")}]"
        
        for c in s:
            if(c in openB):
                stack.append(c)
            else:
                if len(stack)==0:
                    return False
                if c  == ")" and stack[-1] == "(":
                    stack.pop(-1)
                elif c == "}" and stack[-1] == "{":
                    stack.pop(-1)
                elif c == "]" and stack[-1] == "[":
                    stack.pop(-1)
                else:
                    return False
        
        
        return len(stack)==0