
class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
 
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = None  # Real head (least recent)
        self.tail = None  # Real tail (most recent)
 
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        
        # REMOVE from current position
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next  # node was head
        
        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev  # node was tail
        
        # ADD to tail (most recent)
        node.prev = self.tail
        node.next = None
        
        if self.tail:
            self.tail.next = node
        else:
            self.head = node  # First node in list
        
        self.tail = node
        
        return node.val
 
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            
            # REMOVE from current position
            if node.prev:
                node.prev.next = node.next
            else:
                self.head = node.next
            
            if node.next:
                node.next.prev = node.prev
            else:
                self.tail = node.prev
            
            # ADD to tail
            node.prev = self.tail
            node.next = None
            
            if self.tail:
                self.tail.next = node
            else:
                self.head = node
            
            self.tail = node
        else:
            # Evict LRU if at capacity
            if len(self.cache) >= self.capacity:
                lru_node = self.head
                
                # REMOVE LRU node
                if lru_node.next:
                    lru_node.next.prev = None
                    self.head = lru_node.next
                else:
                    self.head = None
                    self.tail = None
                
                del self.cache[lru_node.key]
            
            # ADD new node
            node = Node(key, value)
            self.cache[key] = node
            
            # ADD to tail
            node.prev = self.tail
            node.next = None
            
            if self.tail:
                self.tail.next = node
            else:
                self.head = node  # First node
            
            self.tail = node
 