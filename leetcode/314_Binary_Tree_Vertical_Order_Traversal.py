from collections import queue, defaultdict
def verticalOrder(root):
    """
    :type root: Optional[TreeNode]
    :rtype: List[List[int]]
    Approach:
    track both vertical and horizontal position
    we can use BFS because it processes by level
    can use a queue to manage the traversal
    root starts at column, column -1 is left node,
    column + 1 is right node.
    we will use a defaultdict to process them by column index
    Columns are then sorted by their indices, which will give us
    the vertical order.
    """
    #Store by column index
    result = defaultdict(list)
    #Queue to perform BFS by (node, column index)
    queue = deque([(root, 0)])
    while queue:
        #Get the current node and its position
        node, pos = queue.popleft()
        if node:
            #add node's value to corresponding column
            result[pos].append(node.val)
            #Left goes to column -1
            #Right goes to column + 1
            queue += (node.left, pos-1), (node.right, pos+1)
    #Sort by column index and return values in result
    return [result[i] for i in sorted(result)]
