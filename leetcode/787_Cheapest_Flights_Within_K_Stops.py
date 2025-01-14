from collections import defaultdict, deque

def findCheapestPrice(n, flights, src, dst, k):
    """
    :type n: int
    :type flights: List[List[int]]
    :type src: int
    :type dst: int
    :type k: int
    :rtype: int
    """
    #Build adjacency list rep of the graph
    #Each entry will store (destination, price)
    graph = defaultdict(list)
    for from_city, to_city, price in flights:
        graph[from_city].append((to_city, price))
    
    #Queue will store (city, total_cost, stops)
    queue = deque([(src, 0, 0)])

    #Keep track of minimum cost to reach each city
    #We need ro track costs at each level because a more expensive path
    #with fewer stops might lead to a cheaper overall solution
    min_costs = [float('inf')] * n
    min_costs[src] = 0

    while queue:
        city, total_cost, stops = queue.popleft()

        #If we've used more than k stops, skip
        if stops > k:
            continue
        
        #Check all neighboring cities
        for next_city, price in graph[city]:
            next_cost = total_cost + price
            
            #Only process if:
            #1. We haven't exceeded stops limit
            #2. New cost is cheaper than known cost to reach next_city
            #OR we've reached it in fewer stops
            if stops <= k and next_cost < min_costs[next_city]:
                min_costs[next_city] = next_cost
                queue.append((next_city, next_cost, stops + 1))
    return min_costs[dst] if min_costs[dst] != float('inf') else -1

    #time O(n * k)
    #space O(n)
