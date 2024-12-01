def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    counter
    [2,2,2,3,4,4,5,5,5,5] k = 3
    {2:3, 3:1, 4:2, 5:3}
    [] to keep top k elements
    [(3,2),(2,4), (3,5)]
    [2,3,4]
    """
    #store our frequencies
    freq_map = Counter(nums)

    #use a min-heap to keep top k elements
    heap = []
    for num, freq in freq_map.items():
        heapq.heappush(heap, (freq, num))
        if len(heap) > k:
            heapq.heappop(heap)
    
    #extract the elements from the heap
    return [num for freq,num in heap]

    #time O()
    #O(n) counting freqs, O(u log k), u is number of unique
    #elements, and k is heap size
    #extract results O(k)
    #total O(n + u log k) O(n log k)

    #space freq map O(u), heap O(k), total O(u + k)
