def longestPalindrome(s: str) -> str:
    res = ""

    def expand(l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        
        return s[l+1:r]
    
    for i in range(len(s)):
        # expand around single center
        tmp = expand(i, i)
        if len(tmp) > len(res):
            res = tmp

        # expand around double center
        tmp = expand(i, i+1)
        if len(tmp) > len(res):
            res = tmp

    return res

# not really dp
print(longestPalindrome("ababd"))