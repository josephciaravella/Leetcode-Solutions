def lengthOfLongestSubstring(s: str) -> int:
    sub = ""
    longest = 0
    l, r = 0, 0
    while r < len(s) and l < len(s):
        if s[r] not in sub:
            sub += s[r]
            r += 1
        else:
            if s[r] == sub[0]:
                sub = sub[1:] + s[r] 
                l += 1
                r += 1
            else:
                while s[l] != s[r]:
                    sub = sub[1:]
                    l += 1

        if len(sub) > longest:
            longest = len(sub)
        
    return longest

print(lengthOfLongestSubstring("xyzxyzxyz"))