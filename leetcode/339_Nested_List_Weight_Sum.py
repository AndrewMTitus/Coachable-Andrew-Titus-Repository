def depthSum(nestedList):
    """
    :type nestedList: List[NestedInteger]
    :rtype: int
    use a recursive depth-first search to traverse a nested list
    multiplying each integer by its depth level. 
    At each recursive call, the depth increases by 1 when entering a
    nested list, allowing the algorithm to calculate the weighted sum
    of integers based on their nested level. 
    The base case is when an integer is found, at which point it's
    multiplied by the current depth and added to the total sum.
    """
    def dfs(nestedList, depth):
        total = 0
        for item in nestedList:
            if item.isInteger():
                total += item.getInteger() * depth
            else:
                total += dfs(item.getList(), depth +1)
        return total
    return dfs(nestedList, 1)
