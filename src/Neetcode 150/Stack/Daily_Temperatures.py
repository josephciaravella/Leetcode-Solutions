def dailyTemperatures(temperatures):
    res = [0 for _ in range(len(temperatures))]
    if len(temperatures) == 1:
        return [0]

    stack = []
    for i in range(len(temperatures)):
        if not stack:
            stack.append(i)
            continue
        peek = temperatures[stack[-1]]
        while stack and temperatures[i] > peek:
            top = stack.pop()
            res[top] = i - top
            if stack:
                peek = temperatures[stack[-1]]
        stack.append(i)


    return res

dailyTemperatures([30,40,50,60])