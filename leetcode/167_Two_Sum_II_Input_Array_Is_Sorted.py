def twoSum(numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    we can perform a binary search
    where we have a left and right pointer. 
    The left at the beginning of the array,
    the right at the end of it. 
    We check if the sum of these two points
    equals the target and if so return the left
    and right index + 1, since it is 1-indexed. 
    If it is less than the target move left, 
    if it is greater move the right pointer.
    """
    left, right = 0, len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == target:
            return [left + 1, right + 1]
        if current_sum < target:
            left += 1
        else:
            right -= 1
    return None
        #time O(n) each element is visited once.
        #space O(1) no additional space used16
