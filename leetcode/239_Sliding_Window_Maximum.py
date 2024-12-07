class Solution(object):
    from collections import deque
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        Sliding window:
        1. Maintain a deque to  store the indices  of array elements,
        where the deque always contains elements in decreasing order.
        The first element in the deque is always the maximum in the current window.
        2. Remove elements out of the window from the deque as the window slides.
        3.Add each new element to the deque while maintaining the decreasing order.
        """
        if not nums or k == 0:
            return []
        
        #Initialize deque and result array
        deq = deque()
        result = []

        for i in range(len(nums)):
            #Remove indices that are out of window.
            if deq and deq[0] < i - k + 1:
                deq.popleft()
            
            #Remove smaller numbers in k range
            while deq and nums[deq[-1]] < nums[i]:
                deq.pop()
            
            #Add the current element's index
            deq.append(i)

            #Add the maximum of the current window
            #to the result list
            if i >= k - 1:
                result.append(nums[deq[0]])
        return result

        #time O(n) for each element in the array
        #space O(k) for the deque
