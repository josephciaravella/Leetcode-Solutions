def evalRPN(tokens) -> int:
    stack = []
    operators = ["+", "-", "*", "/"]

    if len(tokens) == 1:
        return int(tokens[-1])

    for char in tokens:
        if char not in operators:
            stack.append(char)
        else:
            b = int(stack.pop())
            a = int(stack.pop())

            if char == "+":
                stack.append(a + b)
            elif char == "-":
                stack.append(a - b)
            elif char == "*":
                stack.append(a * b)
            elif char == "/":
                stack.append(int(a / b))

    return stack[0]

evalRPN(["1","2","+","3","*","4","-"])