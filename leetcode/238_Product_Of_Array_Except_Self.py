def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    the key idea to solving this is passing over the array 
    twice. In the first pass, we create an array of 1's and 
    accumulate products of elements to the left. Then we pass
    from the right and accumulate products of elements to the 
    right by using the left pass resulting array. 
    Ex: nums = [1,3,5,7]
    answer(new array) = [1,1,1,1] -> nothing to left of 1, so
    1 * 1 = 1. at index 1, 1 is left to 1, so again, 1 * 1 = 1
    at index 2, 3 and 1 are to the left. 3*1 = 3. at index 3, 
    5,3,1 and 1 are to the left. 5*3*1 = 15. Therefore, the
    new array after the left pass is [1,1,3,15].
    Now we go over this array again but starting from the 
    right with this new array. Nothing to the right of 15 at
    index 3, so it remains 15. At index 2, 7 is to the right
    of 5, 7*3 = 21. At index 1, the numbers to the right are
    5 and 7. So, 1*5*7 = 35. Finally, at index 0, the numbers
    to the right are 3, 5, and 7. 1*3*5*7 = 105. We can now
    return our answer which is [105, 35, 21, 15].
    """
    n = len(nums)

    #create array for answer
    answer = [1] * n

    #calculate left product
    left = 1
    for i in range(n):
        answer[i] = left
        left *= nums[i]
        
    #calculate right product
    right = 1
    for i in range(n -1, -1, -1):
        answer[i] *= right
        right *= nums[i]
        
    return answer

    #time O(n) two passes over the array
    #space O(1) the answer array is not considered extra space
