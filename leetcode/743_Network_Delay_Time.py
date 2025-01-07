from collections import defaultdict
import heapq

def networkDelayTime(times, n, k):
    """
    :type times: List[List[int]]
    :type n: int
    :type k: int
    :rtype: int
    We can apply Dijkstra's algorithm to find the shortest path from
    a single source node to all other nodes in a weighted directed graph.
    """
    #Create adjacency list using default dict
    #Each entry maps a source node to a list of (target, weight) pairs
    graph = defaultdict(list)
    for source, target, weight in times:
        graph[source].append((target, weight))
    
    #Initialize distances
    distances = {i: float('inf') for i in range(1, n + 1)}
    distances[k] = 0

    #Priority queue to store (distance, node)
    pq = [(0, k)]

    #Set to keep track of visited nodes
    visited = set()

    #Dijkstras's algorithm
    while pq and len(visited) < n:
        curr_dist, curr_node = heapq.heappop(pq)

        #Skip if node already visited
        if curr_node in visited:
            continue
        
        #Mark node as visited
        visited.add(curr_node)

        #Explore neighbors
        for next_node, weight in graph[curr_node]:
            distance = curr_dist + weight

            #Update distance if shorter path is found
            if distance < distances[next_node]:
                distances[next_node] = distance
                heapq.heappush(pq, (distance, next_node))
    
    #Check if all nodes were reached
    if len(visited) < n:
        return -1
    
    #Return maximum distance (time for signal to reach furthest node)
    max_time = max(distances.values())
    return max_time if max_time != float('inf') else -1

    #time O(E * log(N)) E is the number of edges.
    # N is the number of nodes

    #space O(N + E) for the adjacency list and priority queue
