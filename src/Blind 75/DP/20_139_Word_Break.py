def wordBreak(s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        memo = [False]*(len(s)+1)
        memo[len(s)] = True
        for i in range(len(s)-1, -1, -1):
            for word in wordDict:
                if i + len(word) > len(s):
                    continue
                else:
                    if (s[i:i+len(word)] == word):
                        memo[i] = memo[i+len(word)]
                    if memo[i]:
                        break
        
        return memo[0]