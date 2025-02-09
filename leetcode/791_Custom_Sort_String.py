def customSortString(order, s):
    """
    :type order: str
    :type s: str
    :rtype: str
    create a dictionary and enumerate order so each char is assigned
    a position.
    use a helper function to find correct sorting
    turn s to a list for easier sorting
    use sort function and sort by the get_position helper function
    turn s back into a string and return
    "adcbfe" "sbadecfr"
    unknown elements are sorted at the end
    O(n log n) time due to sorting and O(n) space for storing the list.
    {a:1, d:2, c:3, b:4, f:5, e:6}
    [sbadecfr]
    [adcbfesr]
    "adcbfesr"
    """
    char_dict = {c:i for i, c in enumerate(order)}
    def get_position(char):
        return char_dict.get(char, len(order))
    s_list = list(s)
    s_list.sort(key=get_position)
    return ''.join(s_list)
