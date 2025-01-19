def minDistance(word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: int
    """
    #Create a matrix with dimensions (m+1) x (n+1)
    # where m and n are lengths of word1 and word2 respectively
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    #Initialize row and column
    for i in range(m + 1):
        dp[i][0] = i #Cost of deleting characters from word1
    for j in range(n + 1):
        dp[0][j] = j #Cost of inserting characters from word2
    
    #Fill the matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i-1] == word2[j-1]:
                #Characters match, no operation needed
                dp[i][j] = dp[i-1][j-1]
            else:
                #Take minimum of three operations
                #Replace: dp[i-1][j-1]
                #Delete: dp[i-1][j]
                #Insert: dp[i][j-1]
                dp[i][j] = 1 + min(dp[i-1][j-1],
                                dp[i-1][j],
                                dp[i][j-1])
    return dp[m][n]

    #time O(m*n)
    #space O(m*n)
