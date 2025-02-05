def simplifyPath(path):
    """
    :type path: str
    :rtype: str
    we first split the string by /
    we use a stack to keep track of which items to add and which
    to ignore.
    If we see an empty string or '.' then continue iterating
    If we see '..' and the stack has something inside it, then pop
    the last element from the stack
    Anything else we just add to the stack.
    After we are done iterating, then we join the stack back into 
    a string by a slash, so that a slash will precede each element.
    """
    components = path.split('/')
    stack = []

    for component in components:
        if component == '' or component == '.':
            continue
        elif component == '..':
            if stack:
                stack.pop()
        else:
            stack.append(component)
    canonical_path = '/' + '/'.join(stack)
    return canonical_path
