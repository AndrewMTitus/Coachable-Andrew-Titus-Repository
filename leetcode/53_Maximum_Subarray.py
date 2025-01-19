def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    #Edge case: if array has only one element
    if len(nums) == 1:
        return nums[0]
    
    current_sum = max_sum = nums[0]

    #Iterate through the array starting from second element
    for num in nums[1:]:
        #For each element, we have two choices:
        #1. Start a new subarray with current number
        #2. Add current number to existing subarray
        current_sum = max(num, current_sum + num)

        #Update maximum sum if current sum is larger
        max_sum = max(max_sum, current_sum)

    return max_sum

    #time O(n)
    #space O(1)
