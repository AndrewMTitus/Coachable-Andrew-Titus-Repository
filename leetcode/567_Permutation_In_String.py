class Solution(object):
    from collections import Counter
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        sliding window technique:
        1. use a counter for s1 and for the window
        2. slide window on s2
        3. if match, return T.
        """
        if len(s1) > len(s2):
            return False
        
        s1_count = Counter(s1)
        window_count = Counter(s2[:len(s1)])

        #Slide the window across s2
        for i in range(len(s1), len(s2)):
            if s1_count == window_count:
                return True
            
            #Update the window: remove the left character
            #and add the right character
            left_char = s2[i - len(s1)]
            window_count[left_char] -= 1
            if window_count[left_char] == 0:
                del window_count[left_char]
            
            window_count[s2[i]] += 1
        
        #Final check for the last window
        return s1_count == window_count

        #time O(n) iterate string once
        #space O(1) freq map size is constant.
