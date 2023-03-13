# In-Memory Cache Library

This is an implementation of an in-memory caching library in Python with support for multiple standard eviction policies. The library is thread-safe and can be used in multi-threaded applications.

## Features

- Support for multiple standard eviction policies (FIFO, LRU, LIFO)
- Support to add custom eviction policies
- Thread safety

## Requirements

Python 3.x

## Installation

To install the library, you can clone the repository or download the source code and import the Cache class into your project.

## Usage

```python
from in_memory_cache import Cache

# Create a cache with capacity 10 and LRU policy
cache = Cache(10, policy='LRU')

## Add items to the cache
cache.set("Key1", "Value1")
cache.set("Key2", "Value2")

## Get values from the cache
print(cache.get("Key1")) # Output: Value1
print(cache.get("Key2")) # Output: Value2

# Clear the cache
cache.clear()
```

## API Reference

### `Cache(capacity, policy)`

Creates a new cache instance with the given capacity and policy.

**Arguments**

- `capacity:` The maximum number of items that can be stored in the cache. **Default** value is 3.

- `policy:` The eviction policy to use. The available options are 'FIFO', 'LRU', and 'LIFO'. The default value is 'LRU'. **Default** value is 'LRU'.

### `set(key, value)`

Adds an item to the cache with the given key and value.

**Arguments**

- `key:` The key for the item.
- `value:` The value for the item.

### `get(key)`

Retrieves the value for the item with the given key. Returns None if the item is not found in the cache.

**Arguments**

- `key:` The key for the item.

### `clear()`

Clears all items from the cache.

## Testing

The library comes with unit tests to ensure that the implementation is correct. You can run the tests by executing the script in the terminal or command prompt.

```bash
python tests_in_memory_cache.py
```
