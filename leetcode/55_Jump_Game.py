def canJump(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    #Initialize the maximum reachable position
    max_reach = 0

    #Iterate through the array
    #We only need to check up to the second-to-last element
    #since we can reach the last element, we're done
    for i in range(len(nums)):
        #If current position is beyond the maximum reach, return False
        if i > max_reach:
            return False
        
        #Update maximum reach for current position
        #max_reach is the maximum of:
        #1. Current max_reach
        #2. Current position + jump length at current position
        max_reach = max(max_reach, i + nums[i])

        #If we can already reach the last index, return True
        if max_reach >= len(nums) - 1:
            return True
    return True

    #time O(n) for the array length
    #space O(1) only use single variable for maximum reach
