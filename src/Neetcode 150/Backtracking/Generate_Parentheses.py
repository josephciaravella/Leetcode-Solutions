def generateParenthesis(n: int):
    res = []

    def backtrack(path, op, cl):
        if op == cl and len(path) == n*2:
            res.append(path)
            return
        
        if op < n:
            backtrack(path + "(", op+1, cl)

        if cl < op:
            backtrack(path + ")", op, cl+1)



    backtrack("", 0, 0)
    return res

generateParenthesis(2)
