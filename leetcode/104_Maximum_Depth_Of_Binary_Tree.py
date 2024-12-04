def maxDepth(root):
    """
    :type root: Optional[TreeNode]
    :rtype: int
    if the node is None, the depth is 0
    recursion to find the depth of left and right
    add 1 to our max depth
    """
    if not root:
        return 0
    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)

    return 1 + max(left_depth, right_depth)
    #time O(N) for number of nodes
    #space O(H) for height of tree due to recursion stack
