def lengthOfLongestSubstring(s: str) -> int:
    sub = ''
    max_len = 0

    for char in s:
        if char not in sub:
            sub += char
            max_len = max(max_len, len(sub))
        else:
            while sub[0] != char:
                sub = sub[1:]
            sub = sub[1:]
            sub += char

    return max_len

lengthOfLongestSubstring("aab")