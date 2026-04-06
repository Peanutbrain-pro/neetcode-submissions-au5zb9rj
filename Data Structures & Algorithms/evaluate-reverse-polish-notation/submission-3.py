class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        for t in tokens:
            if t.lstrip('-').isdigit():
                stack.append(int(t))
            else:
                b = stack.pop()
                a = stack.pop()
                if t == '+':
                    stack.append(a + b)
                elif t == "-":
                    stack.append(a - b)
                elif t == "*":
                    stack.append(a * b)
                else:
                    stack.append(int(a / b))
        
        return stack.pop()
       