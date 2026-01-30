def checkInclusion(s1: str, s2: str) -> bool:
    if len(s1) > len(s2):
        return False
    s1_f = {}
    for char in s1:
        s1_f[char] = s1_f.get(char, 0) + 1

    # build first window
    s2_f = {}
    for i in range(len(s1)):
        s2_f[s2[i]] = s2_f.get(s2[i], 0) + 1


    l, r = 0, len(s1)-1

    if s2_f == s1_f:
            return True
    while r < len(s2)-1:
        s2_f[s2[l]] -= 1
        if s2_f[s2[l]] == 0:
            del s2_f[s2[l]]

        l += 1
        r += 1

        s2_f[s2[r]] = s2_f.get(s2[r], 0) + 1

        if s2_f == s1_f:
            return True


    return False

checkInclusion("adc", "dcda")