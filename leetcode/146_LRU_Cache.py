class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.cache = {}
        self.head = Node()  # Dummy head
        self.tail = Node()  # Dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_node(self, node):
        """Add the node right after the head."""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        """Remove an existing node from the linked list."""
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def _move_to_head(self, node):
        """Move a node to the head of the linked list."""
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self):
        """Pop the current tail node (least recently used)."""
        res = self.tail.prev
        self._remove_node(res)
        return res

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._move_to_head(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._move_to_head(node)
        else:
            if self.size == self.capacity:
                tail = self._pop_tail()
                del self.cache[tail.key]
                self.size -= 1
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_node(new_node)
            self.size += 1
