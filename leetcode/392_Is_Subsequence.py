def isSubsequence(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    we can iterate though t using a pointer for s and t where
    they both start at the first position. t always moves 
    forward, but s only moves forward if there is a match.
    if the pointer for s reaches the end of the s string then
    all characters in t were found, so return true. Otherwise
    we return False.
    """
    pointer_s, pointer_t = 0, 0
    while pointer_s < len(s) and pointer_t < len(t):
        if s[pointer_s] == t[pointer_t]:
            pointer_s += 1
        pointer_t += 1
    return pointer_s == len(s)
    #time O(n) for the length of t
    #space O(1) no extra space used or needed.
