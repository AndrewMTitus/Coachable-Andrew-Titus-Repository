def shortestPathBinaryMatrix(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    We first check if the starting cell or the last cell are blocked,
    if so we return -1 as it is not possible.
    If it possible, we continue by using BFS to find the shortest path.
    We start by using a double-ended queue which will store the row,
    column, and path length. The path length will be the number of
    cells visited so far.
    For each cell, we explore all 8 possible directions:
    Right, Right-Down, Down, Left-Down, Left, Left-Up, Up, Right-Up.
    For each direction, we check if each new position is within bounds,
    Verify that the cell is unvisited(contains 0), and
    If valid we then mark it as visited and add it to the queue and
    increase the path length.
    Once we reach the target cell(n-1, n-1), we have found the shortest
    path and we return the path length. If not, return -1.
    The time will be O(n^2) where n is the dimension of the grid.
    The space will also be O(n^2) for the queue in the worst case where
    we need to traverse every cell.
    """
    n = len(grid)
    #Check if start or end cell is blocked
    if grid[0][0] == 1 or grid[n-1][n-1] == 1:
        return -1
    #Set our directions
    directions = [
        (0,1), (1,1), (1,0), (1,-1),
        (0,-1), (-1,-1), (-1,0), (-1,1)
    ]

    #Create queue for BFS storing row, col, path_length
    queue = deque([(0,0,1)])
    #Mark start as visited
    grid[0][0] = 1

    while queue:
        row, col, path_len = queue.popleft()
        #If target cell reached
        if row == n-1 and col == n-1:
            return path_len
        #Check all 8 directions
        for dx, dy in directions:
            new_row, new_col = row + dx, col + dy
            #Check if the new position is valid
            if (0 <= new_row < n and
                0 <= new_col < n and
                grid[new_row][new_col] == 0):
                #Mark it as visited and add to queue
                grid[new_row][new_col] = 1
                queue.append((new_row, new_col, path_len + 1))
    #If we arrive here, it means no viable path
    return -1
