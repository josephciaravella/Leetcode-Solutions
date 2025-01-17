def characterReplacement(s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    l, r = 0, 0
    longest = 0
    max_freq = 0
    char_freq = {}

    while l < len(s) and r < len(s):
        if s[r] not in char_freq:
            char_freq[s[r]] = 1
        else:
            char_freq[s[r]] += 1
        
        max_freq = max(max_freq, char_freq[s[r]])
        while (r-l+1) - max_freq > k:
            char_freq[s[l]] -= 1
            l += 1
            max_freq = max(char_freq.values())
        
        if (r-l+1) > longest:
            longest = r-l+1
        
        r += 1

    
    return longest


print(characterReplacement("ABAB", 2)) #4
print(characterReplacement("AABABBA", 1)) #4
print(characterReplacement("AAABABB", 1)) #5