def minRemoveToMakeValid(s):
    """
    :type s: str
    :rtype: str
    Approach:
    Turn the string into a list for easier traversal.
    Use a stack to process opening and closing parentheses.
    Traverse the list
    If a closing ) match is paired with an opening ( then pop
    from stack.
    If there are still unmatched opening brackets in stack,
    we remove them by traversing the stack and then 
    turning them into an open string.
    turn back into a string, now with removed unwanted parentheses
    """
    chars = list(s)
    stack = []
    for i in range(len(chars)):
        if chars[i] == '(':
            stack.append(i)
        elif chars[i] == ')':
            if stack:
                stack.pop()
            else:
                chars[i] = ''
    for idx in stack:
        chars[idx] = ''
    return ''.join(chars)
