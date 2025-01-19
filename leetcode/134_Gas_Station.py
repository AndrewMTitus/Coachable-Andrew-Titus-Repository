def canCompleteCircuit(gas, cost):
    """
    :type gas: List[int]
    :type cost: List[int]
    :rtype: int
    """
    #If total gas is less than total cost, impossible to complete circuit
    if sum(gas) < sum(cost):
        return -1
    
    start = 0 # potential starting point
    tank = 0 # current gas in tank

    for i in range(len(gas)):
        tank += gas[i] - cost[i]

        #If we can't reach next station
        if tank < 0:
            #All stations before i+1 can't be the answer
            #Because even if we started with some gas, we'd still fail here
            start = i + 1
            tank = 0
    return start

    #time O(n) for number of gas stations
    #space O(1) only use constant amount of space
