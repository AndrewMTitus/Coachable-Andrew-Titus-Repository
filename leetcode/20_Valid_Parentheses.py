def isValid(s):
    """
    :type s: str
    :rtype: bool
    we can use a stack to keep track of open and closed
    brackets. we need to use a dictionary to map closing 
    brackets to open ones. 
    if the character is an closing bracket, check to see if 
    the stack is empty, if so, return false, as there is no
    matching bracket. 
    pop the top of the stack to see if it matches the current
    closing bracket, if not, return false.
    after the loop is closed, if the stack is empty, return 
    true, as all brackets have been matched. if not, then
    return false.
    """
    brackets = {')': '(', '}': '{', ']': '['}
    stack = []

    for char in s:
        if char in brackets:
            top = stack.pop() if stack else '#'
            if brackets[char] != top:
                return False
        else:
            stack.append(char)
    return not stack
    #time O(n) for the length of s, as we iterate through the
    #string exactly once.

    #space O(n) for worst case if all characters are 
    #open brackets.
