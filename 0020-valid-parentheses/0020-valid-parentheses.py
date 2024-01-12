class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openP = '({['
        
        for i in s:
            if i in openP:
                stack.append(i)
            elif i == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            elif i == ']':
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
            elif i == '}':
                if stack and stack[-1] == '{':
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0