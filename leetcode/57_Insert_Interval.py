def insert(intervals, newInterval):
    """
    :type intervals: List[List[int]]
    :type newInterval: List[int]
    :rtype: List[List[int]]
    """
    result = []
    i = 0
    n = len(intervals)

    #Add all intervals that end before newInterval starts
    while i < n and intervals[i][1] < newInterval[0]:
        result.append(intervals[i])
        i += 1
    
    #Merge all overlapping intervals
    while i < n and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1
    
    #Add the merged interval
    result.append(newInterval)

    #Add remaining interval
    while i < n:
        result.append(intervals[i])
        i += 1
    
    return result

    #time O(n) number of intervals
    #space O(n) store all intervals in worst case
