#Linear probing solution for hashmap exercise
class FixedHashMapOpenAddressing:
    def __init__(self, max_size):
        self.max_size = max_size
        self.size = 0
        self.buckets = [None] * max_size
        self.min_key = None
        self.max_key = None
    
    def _hash(self, key):
        #A simple hash function for string
        return sum(ord(char) for char in key) % self.max_size
        
    def put(self, key, value):
        #Inserts a key-value pair into the hashmap
        if self.size >= self.max_size:
            print("Error: Hashmap is full.")
            return
        
        index = self._hash(key)
        
        #Update min and max keys
        if self.min_key is None or key < self.min_key:
            self.min_key = key
        if self.max_key is None or key > self.max_key:
            self.max_key = key
        
        #Linear probe until an empty slot is found
        while self.buckets[index] is not None:
            if self.buckets[index][0] == key:
                #Updates the key, value
                self.buckets[index] = (key, value)
                return
            index = (index + 1) % self.max_size
        
        #Insert new key-value pair
        self.buckets[index] = (key, value)
        self.size += 1
            
    def get(self, key):
        #Retrieves the value associated with a key
        index = self._hash(key)
        
        while self.buckets[index] is not None:
            if self.buckets[index][0] == key:
                return self.buckets[index][1]
            index = (index + 1) % self.max_size
        
        #If key not found, return None
        return None
        
    def remove(self, key):
        #Removes a key-value pair from a hashmap
        index = self._hash(key)
        
        while self.buckets[index] is not None:
            if self.buckets[index][0] == key:
                self.buckets[index] = None
                self.size -= 1
                return
            index = (index + 1) % self.max_size
    def get_min_key(self):
        #Returns the smallest key in the hashmap
        return self.min_key
        
    def get_max_key(self):
        #Returns the largest key in the hashmap
        return self.max_key

hashmap = FixedHashMapOpenAddressing(10)
hashmap.put("apple", 5)
hashmap.put("banana", 10)
hashmap.put("cherry", 15)

hashmap.get("apple"), 5
hashmap.get("banana"), 10
hashmap.get("cherry"), 15
hashmap.get("date"), None

hashmap.put("apple", 20)
hashmap.get("apple"), 20

hashmap.remove("banana")
hashmap.get("banana"), None

hashmap.get_min_key(), "apple"
hashmap.get_max_key(), "cherry"
