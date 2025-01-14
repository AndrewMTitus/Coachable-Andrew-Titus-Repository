def rob(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    #Handle edge cases
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums[0], nums[1])
    
    #Create helper function
    def rob_linear(houses):
        if len(houses) == 1:
            return houses[0]

        #dp[i] represents maximum money that can be robbed from houses[0:i+1]
        dp = [0] * len(houses)
        dp[0] = houses[0]
        dp[1] = max(houses[0], houses[1])

        for i in range(2, len(houses)):
            #At each house, we can either:
            #1. Skip this house and previous max(dp[i-1])
            #2. Rob this house and add to max from two houses ago (dp[i-2])
            # + houses[i]
            dp[i] = max(dp[i-1], dp[i-2] + houses[i])
        return dp[-1]
    
    #Since houses are in a circle, we have two scenarios:
    #1. Rob first house to second-to-last house
    #2. Rob second house to last house
    #Take maximum of these two scenarios
    return max(
        rob_linear(nums[:-1]), #Exclude last house
        rob_linear(nums[1:]) #Exclude first house
    )

    #time O(n) for the number of houses
    #space O(n) for the dp array
