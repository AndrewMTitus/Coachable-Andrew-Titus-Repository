def longestConsecutive(nums):
    """
    :type nums: List[int]
    :rtype: int
    Insert all numbers from the array into a set. O(1).
    Iterate array, check if its a start of a sequence. 
    If it is the start of a sequence, then count the length.
    Track the maximum length of consecutive sequences.
    """
    if not nums:
        return 0
        
    num_set = set(nums)
    longest_streak = 0

    for num in num_set:
        #check if its the start of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            #count the length of the sequence
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1
            longest_streak = max(longest_streak, current_streak)

    return  longest_streak

    #time O(n) each number is added to the set and processed
    #once.
    #space O(n) for the storage of the set.
