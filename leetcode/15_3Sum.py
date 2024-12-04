def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    we can solve using a fixed pointer and 
    a two-pointer tecnique. 
    1. Sort the array to avoid duplicate 
    triplets and to use the two-pointer technique.
    2. Fix one element. Iterate and fix one 
    number(nums[i]) and use two pointers, left and right, 
    to find pairs that the sum equals -nums[i].
    3. Use the two pointers to search for pairs 
    whose sum equals the target and adjust pointers 
    based on the sum.
    4. Skip duplicate values while iterating to 
    ensure unique triplets. 
    """
    nums.sort() #sort the array
    result = []
    n = len(nums)

    for i in range(n):
        #skip duplicates for the first number
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        #use two-pointer technique
        left, right = i + 1, n - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                #skip duplicates for second and third numbers
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    return result
    #time O(n^2) sorting takes O(n log n), and the
    #two-pointer search for each element takes O(n),
    #resulting in O(n^2)
    #space O(1) no additional space used.
