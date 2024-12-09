"""
Use two stacks, a main stack to store all elements
and a min stack to store the minimum element as it
corresponds to the state of the main stack.
For each push operation, compare the new element
with the current minimum. Push the smaller value onto the min stack.
For each pop operation, pop elements from both stacks
to maintain synchronization.
For top, return the top of the main stack.
For getMin, return the top of the min stack.
"""
def __init__(self):
    self.stack = [] #Main stack
    self.min_stack = [] #Track minimums

def push(self, val):
    """
    :type val: int
    :rtype: None
    """
    self.stack.append(val)
    #Update the min stack
    if not self.min_stack or val <= self.min_stack[-1]:
        self.min_stack.append(val)

def pop(self):
    """
    :rtype: None
    """
    if self.stack:
        val = self.stack.pop()
    #Synchronize the min stack
    if val == self.min_stack[-1]:
        self.min_stack.pop()

def top(self):
    """
    :rtype: int
    """
    if self.stack:
        return self.stack[-1]
    return None #In case stack is empty

def getMin(self):
    """
    :rtype: int
    """
    if self.min_stack:
        return self.min_stack[-1]
    return None # In case min stack empty
#time O(1) constant, operations are in place.
#space O(n) for storage of stacks.
