class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "-":
                e1 = stack.pop()
                e2 = stack.pop()
                stack.append(e2 - e1)
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "/":
                e1 = stack.pop()
                e2 = stack.pop()
                stack.append(int(e2/e1))
            else:
                stack.append(int(token))
        
        return stack[0]