def climbStairs(n):
    """
    :type n: int
    :rtype: int
    this is a variation of the fibonacci sequence, so we can
    use dynamic programming to solve this one.
    At each step we can take one step from the previous 
    position(n-1) 
    Take 2 steps from the previous position(n-2)
    So the total number of ways is n-1 and n-2.
    """
    if n <= 2:
        return n
        
    #base cases
    first, second = 1, 2

    #calculate ways for each step from 3 up to n
    for _ in range(3, n + 1):
        #update steps to reflect the current step
        first, second = second, first + second
    #'second' holds the result for n
    return second

    #time O(n) we only need to iterate up to n.
    #space O(1) we only use variables first and second.
    #so no extra space needed.
