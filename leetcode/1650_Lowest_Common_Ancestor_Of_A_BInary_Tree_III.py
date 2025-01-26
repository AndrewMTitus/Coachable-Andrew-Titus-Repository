def lowestCommonAncestor(p, q):
    """
    :type node: Node
    :rtype: Node
    store the parents (path) from root to p,
    then check q's path, once it is in the p's path,
    we return q
    """
    path = set()
    while p:
        path.add(p)
        p = p.parent
    while q not in path:
        q = q.parent
    return q
