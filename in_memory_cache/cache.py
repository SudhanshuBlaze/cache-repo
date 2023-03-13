from .policies import LRU, FIFO, LIFO
import threading

class Cache:
    def __init__(self, capacity=3, policy='LRU'):
        self.lock = threading.Lock()
        if policy == 'LRU':
            self.eviction_policy = LRU(capacity)
        elif policy == 'FIFO':
            self.eviction_policy = FIFO(capacity)
        elif policy == 'LIFO':
            self.eviction_policy = LIFO(capacity)
        # elif policy == 'custom':
        #     self.eviction_policy = CustomImplementation(capacity, update_key_on_get, update_key_on_set)
        else:
            raise ValueError("Invalid eviction policy")

    def get(self, key):
        with self.lock:
            return self.eviction_policy.get(key)
        
    def set(self, key, value):
        with self.lock:
            return self.eviction_policy.set(key, value)
    
    def clear(self):
        with self.lock:
            return self.eviction_policy.clear()



