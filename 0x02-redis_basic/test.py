import unittest
from typing import Callable
import redis
Cache = __import__('exercise').Cache

class TestCache(unittest.TestCase):

    def setUp(self):
        """Set up the Cache instance for testing"""
        self.cache = Cache()

    def test_store_and_retrieve(self):
        """Test storing and retrieving data from the Cache"""
        TEST_CASES = {
            b"foo": None,
            123: int,
            "bar": lambda d: d.decode("utf-8")
        }

        for value, fn in TEST_CASES.items():
            key = self.cache.store(value)
            self.assertEqual(self.cache.get(key, fn=fn), value)

if __name__ == '__main__':
    unittest.main()
