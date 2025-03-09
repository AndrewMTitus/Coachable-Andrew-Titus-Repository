class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class Stack:
  def __init__(self):
    self.first = None

  #add an item to the stack
  def push(self):
    new_node = Node(value)
    new_node.next = self.first
    self.first = new_node
    
  #remove an item from the stack
  def pop(self):
    popped = self.first.value
    self.first = self.first.next
    return poppped
    
  #peeks at top value
  def peek(self):
    return self.first.value
