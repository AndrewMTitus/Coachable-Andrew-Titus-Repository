def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if not strs:
        return ""
    #Start with the first string as the prefix
    #Example, first string is "flower", so we compare
    #"flower to the other strings, "flow" and "flight"
    prefix = strs[0]

    #compare the first string with each string in the array
    for s in strs[1:]:
        #reduce the prefix string until it matches the start
        # of string s
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            #if the prefix becomes empty and does not match
            #then there is no common prefix
            if not prefix:
                return ""
    return prefix
    #time O(s) for the sum of all characters in the string
    # in the worst case where we need to check all characters

    #space O(1) if we ignore the input,output space
