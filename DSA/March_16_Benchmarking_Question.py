#Seperate Chaining solution for hashmap exercise
class Node:
    #Uses a Node for linked list in seperate chaining
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
    
class FixedHashMap:
    #Hashmap using seperate chaining for collision handling
    def __init__(self, max_size):
        self.max_size = max_size
        self.size = 0
        self.buckets = [None] * max_size
        self.min_key = None
        self.max_key = None
    
    def _hash(self, key):
        #Iterate over each character and add up their ASCII value, then modulo the max_size to know which bucket it will go in.
        return sum(ord(char) for char in key) % self.max_size
    
    def put(self, key, value):
        #Inserts a key-value pair into the hashmap
        if self.size >= self.max_size:
            print("Error! Hashmap is full!")
            return
        
        index = self._hash(key)
        node = self.buckets[index]
        #Update min and max keys
        if self.min_key is None or key < self.min_key:
            self.min_key = key
        if self.max_key is None or key > self.max_key:
            self.max_key = key
        
        #If buckey is empty insert directly
        if not node:
            self.buckets[index] = Node(key, value)
            self.size += 1
            return
        
        #Traverse the linked list to handle collisions
        prev = None
        while node:
            if node.key == key:
                node.value = value
                return
            prev = node
            node = node.next
        
        #Append new node to the end of the linked list
        prev.next = Node(key, value)
        self.size += 1
    
    def get(self, key):
        #Retrieves the value associated with a key
        index = self._hash(key)
        node = self.buckets[index]
        
        while node:
            if node.key == key:
                return node.value
            node = node.next
        
        #If key not found, return None
        return None
    
    def get_min_key(self):
        #Returns the smallest key in the hashmap
        return self.min_key
    
    def get_max_key(self):
        #Returns the largest key in the hashmap
        return self.max_key

hashmap = FixedHashMap(10)
hashmap.put("apple", 5)
hashmap.put("banana", 10)
hashmap.put("cherry", 15)

hashmap.get("apple"), 5
hashmap.get("banana"), 10
hashmap.get("cherry"), 15
hashmap.get("date"), None

hashmap.put("apple", 20)
hashmap.get("apple"), 20

hashmap.get_min_key(), "apple"
hashmap.get_max_key(), "cherry"
