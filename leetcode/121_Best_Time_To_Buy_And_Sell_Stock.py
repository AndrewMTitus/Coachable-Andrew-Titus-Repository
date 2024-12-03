def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    prices = [3,9,4,2,8,6]
    6 1 6 4
    [2,3,1,6,7,9,4,8]
    1 5 6 8 3 7
    time O(n)
    space O(1)
    """
    min_profit = float('inf')
    max_profit = 0

    for price in prices:
        if price < min_profit:
            min_profit = price
        elif price - min_profit > max_profit:
            max_profit = price - min_profit
    return max_profit
