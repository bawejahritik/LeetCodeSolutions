class Solution:
    def isValid(self, s: str) -> bool:
        stack =  []
        
        openB = "({["
        closeB = ")]}"
        
        for brack in s:
            if brack in openB:
                stack.append(brack)
            elif stack and (brack in closeB):
                if (brack == ")" and stack[-1]=="(") or (brack=="]" and stack[-1]=="[") or (brack=="}" and stack[-1]=="{"):
                    stack.pop()
                else:
                    return False
            else:
                return False
        
        
        return len(stack)==0
                
                
                    