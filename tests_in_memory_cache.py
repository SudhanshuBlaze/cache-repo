import unittest
from in_memory_cache import Cache

class TestCache(unittest.TestCase):
    def test_get_with_empty_cache(self):
        cache = Cache(capacity=3, policy='LRU')
        
        self.assertIsNone(cache.get('key'))
        
    def test_set_with_empty_cache(self):
        cache = Cache(capacity=3, policy='LRU')
        cache.set('key', 'value')
        
        self.assertEqual(cache.get('key'), 'value')
        
    def test_clear(self):
        cache = Cache(capacity=3, policy='LRU')
        cache.set('key1', 'value1')
        cache.set('key2', 'value2')
        cache.clear()
        
        self.assertIsNone(cache.get('key1'))
        self.assertIsNone(cache.get('key2'))
        
        
    def test_LRU(self):
        cache = Cache(capacity=3, policy='LRU')
        
        for i in range(1, 4):
            cache.set(f'key{i}', f'value{i}')
        cache.get('key1')
        cache.set('key4', 'value4')
        
        self.assertIsNone(cache.get('key2'))
        self.assertEqual(cache.get('key1'), 'value1')
        self.assertEqual(cache.get('key3'), 'value3')
        
    def test_FIFO(self):
        cache = Cache(capacity=3, policy='FIFO')

        for i in range(1, 5):
            cache.set(f'key{i}', f'value{i}')

        self.assertIsNone(cache.get('key1'))
        self.assertEqual(cache.get('key2'), 'value2')
        self.assertEqual(cache.get('key3'), 'value3')
        self.assertEqual(cache.get('key4'), 'value4')
        
    def test_LIFO(self):
        cache = Cache(capacity=3, policy='LIFO')

        for i in range(1, 5):
            cache.set(f'key{i}', f'value{i}')
        
        self.assertIsNone(cache.get('key3'))
        self.assertEqual(cache.get('key2'), 'value2')
        self.assertEqual(cache.get('key1'), 'value1')
        self.assertEqual(cache.get('key4'), 'value4')
        
    def test_invalid_eviction_policy(self):
        with self.assertRaises(ValueError):
            cache = Cache(capacity=3, policy='InvalidPolicy')

if __name__ == '__main__':
    unittest.main()

        
