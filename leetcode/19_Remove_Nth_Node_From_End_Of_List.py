class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next_node
def removeNthFromEnd(head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    # Create a dummy node that points to the head of the list
    dummy = ListNode()
    dummy.next = head
    first = dummy # This pointer will be used to find the end of the list
    second = dummy # This pointer will be behind the first by n + 1 nodes
    # Move the first pointer n + 1 steps ahead so there's a gap of
    #n nodes between first and second pointers
    for _ in range(n + 1):
        first = first.next
    # Move both pointers until the first pointer reaches the end of the list
    # By this time, the second pointer will be just before the node to remove
    while first:
        first = first.next
        second = second.next
    # Remove the nth node from the end by skipping it
    second.next = second.next.next
    # Return the head of the modified list
    return dummy.next
    #time O(n) each element is accessed once.
    #space O(1) no extra used.
