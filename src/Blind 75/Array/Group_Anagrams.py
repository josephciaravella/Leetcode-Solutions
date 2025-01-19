def groupAnagrams(strs):
    groups = {}
    def str_freq(s):
        freq = [0] * 26
        for char in s:
            i = ord(char) - ord('a')
            freq[i] += 1

        return tuple(freq)
    
    for s in strs:
        freq = str_freq(s)
        if freq in groups:
            groups[freq].append(s)
        else:
            groups[freq] = [s]
        
        
    return list(groups.values())