def partition(s: str):
    res = []

    def backtrack(start, path):
        if start == len(s):
            res.append(path[:])
            return

        for i in range(start, len(s)):
            sub = s[start:i+1]
            if sub == sub [::-1]:
                path.append(sub)
                backtrack(i+1, path)
                path.pop()

    backtrack(0, [])
    return res

partition("aab")