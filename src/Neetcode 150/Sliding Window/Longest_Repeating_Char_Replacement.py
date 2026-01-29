def characterReplacement(s: str, k: int) -> int:
    freq = {}    
    l = 0
    max_len = 0
    pop = 0

    for r in range(len(s)):
        char = s[r]

        # update dictionary
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
        
        # update most popular
        pop = max(pop, freq[s[r]])

        while (1+r-l)-pop > k:
            freq[s[l]] -= 1
            l += 1 
            # find most popular
            pop = 0
            for key in freq:
                pop = max(freq[key], pop)

        
        # update max length
        max_len = max(max_len, (1+r-l))
    
    return max_len

print(characterReplacement("ABABBA", 2))