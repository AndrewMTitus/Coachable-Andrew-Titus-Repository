class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        max_length = 0
        left = 0
        freq = defaultdict(int)
        max_freq = 0

        for right in range(len(s)):
            #Add the character at the right pointer to the frequency map
            freq[s[right]] += 1
            #Update the max frequency of a single character in the window
            max_freq = max(max_freq, freq[s[right]])

            #Current window size
            window_size = right - left + 1

            #If changes needed exceed k, shrink the window.
            if window_size - max_freq > k:
                freq[s[left]] -= 1
                left += 1
            
            #Update the max length of valid window
            max_length = max(max_length, right - left + 1)

        return max_length

        #time O(n) each character processed at most twice.
        #space O(1) since the frequency map can have at most 26 keys(Uppercase characters).
