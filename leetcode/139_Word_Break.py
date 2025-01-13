def wordBreak(s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: bool
    """
    #Create a set for O(1) lookup time
    word_set = set(wordDict)

    #dp[i] represents whether s[0:i] can be segmented into words from wordDict
    #Add 1 to handle empty string case
    dp = [False] * (len(s) + 1)

    #Empty string is always valid
    dp[0] = True

    #For each position i in the string
    for i in range(1, len(s) + 1):
        #Try all possible substrings ending at i
        for j in range(i):
            #If we can segment string up to j AND
            #the substring from j to i is in wordDict
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break
    return dp[len(s)]

    #time O(n^3) for two nested loops and slicing takes O(n) time
    #space O(n) for the dp array plus space for the word set
