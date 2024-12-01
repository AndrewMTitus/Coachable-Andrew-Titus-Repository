def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    we can create a set to store seen elements.
    if a duplicate is found then return True, but if we get
    to the end of the array, then return False.
    """
    #create a set to store unique elements
    seen = set()

    for num in nums:
        if num in seen:
            #duplicate found
            return True
        #add the number to the set
        seen.add(num)
    #no duplicates found
    return False

    #time O(n) n is the length of the array. 
    #space O(n) in worst case where all elements are distinct
