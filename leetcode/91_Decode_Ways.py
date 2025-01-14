def numDecodings(s):
    """
    :type s: str
    :rtype: int
    """
    #Edge cases
    if not s or s[0] == '0':
        return 0
    
    #Initialize dp variables for last two positions.
    #dp1 represents i+1 position, dp2 represents i+2 position
    dp1, dp2 = 1, 1

    #Iterate from right to left
    for i in range(len(s) -1, -1, -1):
        #Initialize current position count
        current = 0

        #Check if single digit is valid (1-9)
        if s[i] != '0':
            current += dp1
        
        #Check if two-digit number is valid (10-26)
        if i + 1 < len(s) and (s[i] == '1' or 
        (s[i] == '2' and s[i + 1] <= '6')):
            current += dp2

        #Update dp variables for next iteration
        dp2 = dp1
        dp1 = current

    return dp1

    #time O(n) for length of the string
    #space O(1) constant space is used
