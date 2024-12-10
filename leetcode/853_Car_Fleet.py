def carFleet(target, position, speed):
    """
    :type target: int
    :type position: List[int]
    :type speed: List[int]
    :rtype: int
    """
    n = len(speed)
    v = [(position[i], speed[i]) for i in range(n)]
    v.sort()
    time = [float(target - v[i][0]) / v[i][1] for i in range(n)]

    curr = float('-inf')
    res = 0

    for i in range(n -1, -1, -1):
        if time[i] > curr:
            curr = time[i]
            res += 1
    return res

    #time O(n*log n)
    #space O(n)
