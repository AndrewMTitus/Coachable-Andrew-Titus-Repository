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
    
    #dp[i] represents the maximum money we can rob up to house i
    dp = [0] * len(nums)

    #Initialize the first two values
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    #For each house, we can either
    #1. Rob it and add it to the money from two houses before (dp[i - 2])
    #2. Skip it and keep the money from the previous house (dp[i - 1])
    for i in range(2, len(nums)):
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
    return dp[-1]

    #time O(n) for the number of houses
    #space O(n) for the array
