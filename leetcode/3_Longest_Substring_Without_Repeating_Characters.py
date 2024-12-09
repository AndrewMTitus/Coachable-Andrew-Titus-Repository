"""
sliding window approach. 
1. initialize a set to store characters in the
current window.
2. initialze pointers and max length. left is 0 
to start to point to the beginning of the window
and max_length stores the longest substring found
3. iterate with a right pointer.
4. adjust the left pointer
5. update max_length to the size of the current 
window.
6. return result
"""
def lengthOfLongestSubstring(self, s):
    """
    :type s: str
    :rtype: int
    """
    char_set = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    return max_length

    #time O(n) each element accessed once
    #space O(k) for the storage of unique characters.
