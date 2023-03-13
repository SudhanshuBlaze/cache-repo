from .eviction_policy import EvictionPolicy

class LRU(EvictionPolicy):
    def update_key_on_get(self, key):
        self.order.remove(key)
        self.order.append(key)

    def update_key_on_set(self, key):
        self.order.append(key)

    def evict(self):
        old_key = self.order.pop(0)
        self.cache.pop(old_key)
