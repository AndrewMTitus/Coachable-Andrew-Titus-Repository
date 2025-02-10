def minAddToMakeValid(s):
    """
    :type s: str
    :rtype: int
    We create a stack and for each value, if the stack is empty, then
    add to the stack. If the last position is an open parentheses,
    and the value is a closed parentheses, then pop from the stack.
    If neither of those, then we add to the stack. The len of the
    stack will give us how many parentheses are not valid.
    Time O(n) to iterate through string once.
    Space O(n) in worst case for size of stack.
    """
    stack = []
    for val in s:
        if not stack:
            stack.append(val)
        elif stack[-1] == '(' and val == ')':
            stack.pop()
        else:
            stack.append(val)
    return len(stack)
