def eraseOverlapIntervals(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: int
    """
    if not intervals:
        return 0
    intervals.sort(key=lambda x: x[1])

    non_overlapping = 1
    prev_end = intervals[0][1]

    for start, end in intervals[1:]:
        if start >= prev_end:
            non_overlapping += 1
            prev_end = end
    return len(intervals) - non_overlapping

    #time O(n log n) sorting
    #space O(1) constant space
