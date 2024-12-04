from collections import defaultdict

def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    we can sort each string alphabetically and use the sorted
    string as a key in a dictionary.
    we create a dictionary where keys are the sorted
    versions of strings and the values are lists of strings
    that share the same sorted key.
    Extract the values(list of anagrams) from the dictionary.
    """
    anagram_groups = defaultdict(list)

    for s in strs:
        #sort the string to form the key
        sorted_key = ''.join(sorted(s))
        #append the original string to the correspondinggroup
        anagram_groups[sorted_key].append(s)

    #return the grouped anagrams
    return list(anagram_groups.values())
    #time O(k log k) where k is the average length of each
    #the strings. Iterating over all n strings takes
    # O(n * k log k)

    #space O(n * k) for storing the dictionary and all
    #strings and their groupings.
