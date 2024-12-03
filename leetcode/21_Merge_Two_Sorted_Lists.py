class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next_node
def mergeTwoLists(list1, list2):
    """
    :type list1: Optional[ListNode]
    :type list2: Optional[ListNode]
    :rtype: Optional[ListNode]
    we can iterate through both lists simultaneously and
    add the nodes onto a new list. we compare nodes and 
    whichever node is smaller gets added first. 
    """
    #create a dummy list to serve as the starting point
    #of the merged list
    dummy = ListNode(0)
    current = dummy

    #Loop until one of the lists is empty
    while list1 and list2:
        #choose the smaller value node to add to the
        #merged list.
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    #if there are any remaining nodes attach them
    current.next = list1 if list1 else list2
    #return the next node of the dummy list, which is
    #the head of the merged list
    return dummy.next
    #time O(m + n) since we iterate through 2 lists.
    #space O(1) no extra space used.
