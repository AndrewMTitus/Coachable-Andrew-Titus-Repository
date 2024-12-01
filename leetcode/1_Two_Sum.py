def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    we can use a hash map to store each number as a key and 
    its index as a value. 
    for each num in the index, we calculate the complement,
    which is the target minus the number.
    we then check to see if each complement exists in the map
    if it does, then return the indices as the answer.
    if it does not, store the current num with its index
    in the map. 
    Example: nums = [2,5,8,13] target = 13
    Output: [1,2] 
    Explanation: The indices nums[1] + nums[2] == 13, so
    we return [1,2].
    """
    #create to dictionary to store numbers and indexes as
    #we iterate
    nums_to_index = {}

    #iterate through the list
    for i, num in enumerate(nums):
        #calculate the complement
        complement = target - num

        #check if the complement is already in the dictionary
        if complement in nums_to_index:
            return [nums_to_index[complement], i]
        
        #store the current number with its index
        nums_to_index[num] = i
        
        #time O(n) for the length of nums
        #space O(n) to store at most each num,index in nums
