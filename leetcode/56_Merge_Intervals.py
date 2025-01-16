def merge(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: List[List[int]]
    """
    #Handle empty or single interval cases
    if not intervals:
        return []
    if len(intervals) == 1:
        return intervals
    
    #Sort intervals by start time
    intervals.sort(key=lambda x: x[0])

    result = []
    current = intervals[0]

    for next_interval in intervals[1:]:
        #If current interval overlaps with next interval
        if current[1] >= next_interval[0]:
            #Merge by taking the maximum end time
            current[1] = max(current[1], next_interval[1])
        else:
            #No overlap, add current to result and move to next
            result.append(current)
            current = next_interval
    
    #Add the last interval
    result.append(current)
    return result

    #time O(n log n) for sorting
    #space O(n) for the result array
