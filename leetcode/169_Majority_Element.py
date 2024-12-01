def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    nums [2,2,1,1,1,2,2]
    counter 

    """
    candidate = None
    counter = 0
    for num in nums:
        if counter == 0:
            candidate = num
        counter += 1 if num == candidate else -1

    return candidate
