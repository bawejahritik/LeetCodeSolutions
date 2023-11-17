class Solution:
    def isValid(self, s: str) -> bool:
        openB = "({["

        stack = []
        
        for b in s:
            if b in openB:
                stack.append(b)
            elif b==")" and stack and stack[-1]=="(":
                stack.pop()
            elif b=="}" and stack and stack[-1]=="{":
                stack.pop()
            elif b=="]" and stack and stack[-1]=="[":
                stack.pop()
            else:
                return False
        
        return len(stack)==0
                