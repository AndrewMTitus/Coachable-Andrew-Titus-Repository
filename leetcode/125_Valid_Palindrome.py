def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    the key idea here is to have two pointers, one starting at the first position, and the second starting at last. 
    If the two positions match then continue to move toward the center until either the two positions meet or 
    one of the two positions are not equal. If they are not equal then return False, if they are return True.
    """
    # Filter out non-alphanumeric characters and convert
    # to lowercase
    filtered_s = ''.join(char.lower() for char in s if char. isalnum())

    # Use two pointers to check if the filtered string is a
    #palindrome
    left, right = 0, len(filtered_s) - 1
    while left < right:
        if filtered_s[left] != filtered_s[right]:
            return False
        left += 1
        right -= 1
    return True
    #time O(n) for length of s, we process each character at
    #most twice.

    #space O(n) to store the filtered_s string
