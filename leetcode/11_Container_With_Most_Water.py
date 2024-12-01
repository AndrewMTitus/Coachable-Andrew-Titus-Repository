def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    We can use a two-pointer approach where we calculate the area between the two points and continue to move the shorter line inward. We update the maximum area as we go and then return the max area.
    """
    left, right = 0, len(height) - 1
    max_area = 0
    
    while left < right:
        #Calculate the area
        current_area = min(height[left], height[right]) * (right - left)
        max_area = max(max_area, current_area)
        #Move the pointer pointing to the shorter line
        if height[left] < height[right]:
            left +=1
        else:
            right -= 1
    return max_area

    #time O(n) each element in the array visited once.
    #space O(1) we only use a few variables to store indices and the max area.  
