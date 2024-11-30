def removeDuplicates(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    nums [0,0,1,1,1,2,2,3,3,4]
            i   j            
    return i + 1
    
    """
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i + 1
    #time O(n)
    #space 0(1)
