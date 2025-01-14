def findItinerary(tickets):
    """
    :type tickets: List[List[str]]
    :rtype: List[str]
    """
    #Create adjacency list
    graph ={}
    for src, dst in tickets:
        if src not in graph:
            graph[src] = []
        graph[src].append(dst)
    
    #Sort destinations in lexical order
    for src in graph:
        graph[src].sort()
    
    route = []
    def dfs(airport):
        #Get destinations from current airport
        while graph.get(airport, []):
            next_dest = graph[airport].pop(0) #Get lexically smallest dest
            dfs(next_dest)
        route.append(airport)
    
    dfs("JFK")
    return route[::-1] #Reverse the route to get correct order

    #time O(ElogE) for edges, sorting and traversal
    #space O(n) for recursion
