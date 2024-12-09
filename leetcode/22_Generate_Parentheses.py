def generateParenthesis(self, n):
    """
    :type n: int
    :rtype: List[str]
    we can use a backtracking approach.
    At each step, add an opening parenthesis
    (if it’s count is less than n, or add a closing
    parenthesis ) if it doesn’t exceed the number of previously
    added opening parentheses. Stop when the length of the
    current combination equals 2n.
    """
    def backtrack(S, left, right):
        if len(S) == 2 * n:
            result.append("".join(S))
            return
        if len(S) < n:
            S.append("(")
            backtrack(S, left + 1, right)
            S.pop()
        if right < left:
            S.append(")")
            backtrack(S, left, right + 1)
            S.pop()
    result = []
    backtrack([], 0, 0)
    return result
    #time O(n) calls made
    #space O(n) for recursive stack
