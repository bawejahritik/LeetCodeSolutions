class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = 0
        
        stack = []
        
        for token in tokens:
            if token == "+":
                val = stack.pop() + stack.pop()
                stack.append(val)
            elif token == "-":
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(val2 - val1)
            elif token == "*":
                val = stack.pop() * stack.pop()
                stack.append(val)
            elif token == "/":
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(int(val2 / val1))
            else:
                stack.append(int(token))
        
        
        return stack[0]