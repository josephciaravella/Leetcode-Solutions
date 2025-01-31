def count(s):
    if len(set(s)) == len(s):
        return len(s)

    num = 0

    for i in range(len(s)):
        l, r = i, i
        while l >=0 and r < len(s) and s[l] == s[r]:
            num += 1
            l -= 1
            r += 1

        l, r = i, i+1
        while l >=0 and r < len(s) and s[l] == s[r]:
            num += 1
            l -= 1
            r += 1


    return num