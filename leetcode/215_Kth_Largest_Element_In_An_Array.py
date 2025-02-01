from collections import heapq
def findKthLargest(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    Two approaches work for this problem, one way we can solve is..
    we can use an algorithm called quickselect to solve for this.
    1. Choose a pivot element.
    2. Partition the array such that elements greater than the pivot
    are on the left and smaller than the pivot are on the right.
    3. If the pivot is the kth largest, we return it.
    4. If the pivot's position is greater than k, recurse on the left,
    if lesser, recurse on the right.
    The second approach is to use a min-heap of size k to keep track
    of the k largest elements. We create a min-heap of size k and then
    iterate through the rest of the array. We then check if the
    element is greater than the smallest element, if it is we pop
    the smallest element and then add the new greatest element to the
    heap. Once we are done iterating, we return the smallest element
    in the heap, heap[0], which will be the kth largest element.
    """
    heap = nums[:k]
    heapq.heapify(heap)

    for num in nums[k:]:
        if num > heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, num)
    return heap[0]
