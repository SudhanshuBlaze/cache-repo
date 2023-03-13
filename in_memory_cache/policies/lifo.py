from .eviction_policy import EvictionPolicy

class LIFO(EvictionPolicy):
    def update_key_on_get(self, key):
        pass

    def update_key_on_set(self, key):
        self.order.append(key)

    def evict(self):
        self.cache.pop(self.order.pop())
