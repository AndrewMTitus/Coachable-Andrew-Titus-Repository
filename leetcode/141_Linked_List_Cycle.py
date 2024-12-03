def hasCycle(head):
    """
    :type head: ListNode
    :rtype: bool
    we can use two pointers here. one slow, the other fast.
    the slow pointer starts at the first position, the fast
    pointer starts at the second position. the slow pointer
    will move one position at a time, but the fast position 
    will move two at a time. if the two positions meet in the
    same position, then there is a cycle.
    [3,2,0,-4]
    s. f 
        s    f
        f   s.   
            f. s
    fs  
    """
    if not head or not head.next:
        return False

    slow = head
    fast = head.next

    while slow != fast:
        if not fast or not fast.next:
            return False
        slow = slow.next
        fast = fast.next.next
    return True
    #time O(n) for the number of nodes in the list.
    #space O(1) no extra space used
