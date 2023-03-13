from in_memory_cache import Cache

cache = Cache(capacity=3, policy='LRU')

# setting values
cache.set('key1', 'value1')
cache.set('key2', 'value2')
cache.set('key3', 'value3')

# getting values
print(cache.get('key1')) # Output: 'value1'
print(cache.get('key2')) # Output: 'value2'
print(cache.get('key3')) # Output: 'value3'

# updating values
cache.set('key1', 'new_value1')

# checking updated values
print(cache.get('key1')) # Output: 'new_value1'

# clearing cache
cache.clear()

# checking values after clear
print(cache.get('key1')) # Output: None
print(cache.get('key2')) # Output: None
print(cache.get('key3')) # Output: None

