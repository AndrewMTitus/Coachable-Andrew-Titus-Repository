def findBuildings(heights):
    """
    :type heights: List[int]
    :rtype: List[int]
    If we iterate from right to left, we check if the building to the
    right is higher or not, if it is not then add that building 
    to the result and update the max height. Then sort the results.
    """
    n = len(heights)
    result = []
    max_height = 0
    for i in range(n-1, -1, -1):
        if heights[i] > max_height:
            result.append(i)
            max_height = heights[i]
    return sorted(result)
