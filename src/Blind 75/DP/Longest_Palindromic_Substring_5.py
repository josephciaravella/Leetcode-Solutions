def palindrome(s):

    longest = ""
    longestLen = 0

    for i in range(len(s)):
        # odd
        l, r  = i, i
        while l >=0 and r < len(s) and s[l] == s[r]:
            if (r-l+1) > longestLen:
                longest = s[l:r+1]
                longestLen = r-l+1
            l -= 1
            r += 1
        
        # even
        l, r = i, i+1
        while l >=0 and r < len(s) and s[l] == s[r]:
            if (r-l+1) > longestLen:
                longest = s[l:r+1]
                longestLen = r-l+1
            l -= 1
            r += 1

            
    return longest