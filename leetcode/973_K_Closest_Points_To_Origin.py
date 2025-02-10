def kClosest(points, k):
    """
    :type points: List[List[int]]
    :type k: int
    :rtype: List[List[int]]
    1. Initialize a max-heap
    2. Calculate the squared distance.
    3. Push each squared distance onto the heap.
    4. If the heap exceeds k, then remove the root point as it will
    be the largest.
    5. After we finish iterating, we will be left with the k closest
    points.
    6. Extract the result from the heap.
    Time will be O(n log n) for the number of points
    Space is O(k) for the heap stores at most k elements.
    """
    heap = []
    for (x,y) in points:
        distance = -(x**2 + y**2)
        if len(heap) < k:
            heapq.heappush(heap, (distance, x, y))
        else:
            if distance > heap[0][0]:
                heapq.heappop(heap)
                heapq.heappush(heap, (distance, x, y))
    result = [[x, y] for (distance, x, y) in heap]
    return result
