class Node:
  def __init(self, value):
    self.value = value
    self.next = None

class Queue:
  def __init(self):
    self.front = None #Points to the front of the queue
    self.rear = None #Points to the rear of the queue

  def is_empty(self):
    self.front is None

  def enqueue(self, value):
    new_node = Node(value)
    if self.is_empty():
      #If empty, both front and rear point to the new node
      self.front = self.rear = new_node
    else:
      #Else, add the new node to the rear and update the rear pointer
      self.rear.next = new_node
      self.rear = new_node

  def dequeue(self):
    if self.is_empty():
      raise IndexError("cannot dequeue from an empty queue")
    dequeued = self.front.value
    #We move the front pointer to the next value
    self.front = self.front.next
    #If the queue is empty after we dequeue, we update our rear to None
    if self.front is None:
      self.rear = None
    return dequeued

  def peek(self):
    if self.is_empty():
      raise IndexError("Peek from empty queue")
    return self.front.value
