def removeElement(self, nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    nums [0,1,2,2,3,0,4,2]
    val = 2
    k = 0, 1, 3, 0, 4
    k = 5
    """
    k = 0

    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k

    #time O(n)
    #space 0(1)
