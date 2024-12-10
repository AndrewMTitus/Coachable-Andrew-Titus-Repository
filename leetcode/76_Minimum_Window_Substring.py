from collections import Counter, defaultdict
def minWindow(s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    sliding window technique:
    1. counters for t and window
    2. two pointers left and right to contract and 
    expand the the window.
    3. expand right, contract left when all chars of
    t are present.
    4. check if the count of chars matches the required
    frequency.
    """
    if not s or not t:
        return ""
    #freq map of chars in t
    t_freq = Counter(t)
    required = len(t_freq)

    #window pointers and window frequency
    left, right = 0,0
    window_counts = defaultdict(int)
    formed = 0

    #window length, left, right
    res = float("inf"), None, None

    while right < len(s):
        char = s[right]
        window_counts[char] += 1

        #If current char count matches freq in t
        if char in t_freq and window_counts[char] == t_freq[char]:
            formed += 1

        #try to contract the window until no
        #longer valid
        while left <= right and formed == required:
            char = s[left]

            #update result if this window is
            #smaller than previous ones
            if (right - left + 1) < res[0]:
                res = (right - left + 1), left, right
            #Move the left pointer and reduce
            #the count of this character
            window_counts[char] -= 1
            if char in t_freq and window_counts[char] < t_freq[char]:
                formed -= 1
            #contract the window
            left += 1
        #Expand the window
        right += 1
    return "" if res[0] == float("inf") else s[res[1]: res[2] + 1]

#time O(m + n) We traverse 's' at most twice and each operation inside the loop is constant time.
#space O(n) due to the Counter and defaultdict
