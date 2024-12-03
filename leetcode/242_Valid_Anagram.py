from collections import Counter

def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    we can use a Counter to keep track of the characters and
    their counts.
    """
    return Counter(s) == Counter(t)
    #time O(n) for the length of the strings
    #space O(k) for special characters if needed, practical 
    #space is O(1)
