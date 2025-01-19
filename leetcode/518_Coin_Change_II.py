def change(amount, coins):
    """
    :type amount: int
    :type coins: List[int]
    :rtype: int
    """
    #Initialize dp array with 0s
    #dp[i] represents the ways to make amount i
    dp = [0] * (amount + 1)

    #Base case: there is 1 way to make amount 0 (using no coins)
    dp[0] = 1

    #For each coin, update all possible amounts up to target amount
    for coin in coins:
        #Start from coin value to avoid invalid combinations
        for current_amount in range(coin, amount + 1):
            #Add the number of combinations possible by using the current coin
            dp[current_amount] += dp[current_amount - coin]
    return dp[amount]

    #time O(amount * len(coins))
    #space O(amount)
