def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    nums [0,1,2,2,3,0,4,2]
    val = 2
    k = 0, 1, 3, 0, 4
    k = 5
    """
    k = 0 #pointer for the next position of a non-val element

    for num in nums:
        if num != val:
            nums[k] = num #Keep the element
            k += 1 #Increment the pointer of non-val elements.
    return k
    
    #time O(n)
    #space 0(1)
