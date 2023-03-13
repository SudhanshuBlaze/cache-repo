class EvictionPolicy:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.order = []

    def get(self, key):
        if key in self.cache:
            self.update_key_on_get(key)
            return self.cache[key]
        else:
            return None
        
    def set(self, key, value):
        if len(self.cache) >= self.capacity:
            self.evict()
        self.cache[key] = value
        self.update_key_on_set(key)
        
    def clear(self):
        self.cache = {}
        self.order = []

    def update_key_on_set(self, key):
        raise NotImplementedError

    def update_key_on_get(self, key):
        raise NotImplementedError

    def evict(self):
        raise NotImplementedError