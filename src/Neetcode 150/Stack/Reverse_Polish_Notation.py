class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = ['+', '-', '*', '/']

        if len(tokens) == 1:
            return int(tokens[0])

        if len(tokens) < 3:
            return 0
        
        for token in tokens:
            if token not in operands:
                stack.append(token)
            else:
                b = int(stack.pop())
                a = int(stack.pop())

                if token == '-':
                    stack.append(a-b)
                elif token == '+':
                    stack.append(a+b)
                elif token == '*':
                    stack.append(a*b)
                else:
                    stack.append(int(a/b))

        return stack[0]