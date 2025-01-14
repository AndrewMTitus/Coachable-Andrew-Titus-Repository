def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    We can solve this using the expand around center approach.
    It is more space efficient than dp, where in dp the space would be
    O(n^2). It needs a 2D Array to store intermediate results.
    """
    if not s:
        return ""
    
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1
    
    start = 0
    end = 0

    for i in range(len(s)):
        #Check odd length palindromes with center at i
        len1 = expand_around_center(i, i)
        #Check for even length palindromes with center between i and i+1
        len2 = expand_around_center(i, i + 1)

        #Update the maximum lenght palindrome found
        max_len = max(len1, len2)
        if max_len > (end - start):
            start = i - (max_len - 1) // 2
            end = i + max_len // 2
    return s[start:end + 1]

    #time O(n^2) for the length of the string
    #space O(1) for constant amount of extra space
