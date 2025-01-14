def coinChange(coins, amount):
    """
    :type coins: List[int]
    :type amount: int
    :rtype: int
    """
    #Create dp array filled with amount + 1 (impossible value)
    #dp[i] represents the minimum amount of coins needed for amount i
    dp = [amount + 1] * (amount + 1)

    #Base case: 0 amount needs 0 coins
    dp[0] = 0

    #For each amount from 1 to target amount
    for current_amount in range(1, amount + 1):
        #Try each coin
        for coin in coins:
            #If the coin values is less than or equal to cur amount
            if coin <= current_amount:
                #Take minimum between current solution and
                #solution for (current_amount - coin) + 1
                dp[current_amount] = min(
                    dp[current_amount],
                    dp[current_amount - coin] + 1
                )
    
    #Return -1 if no solution found, else return solution
    return dp[amount] if dp[amount] != amount + 1 else -1

    #time O(amount * len(coins))
    #space O(amount)
