#!/usr/bin/env python3
"""Comment"""
import uuid
import redis
from typing import Union, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Decorator method"""
    @wraps(method)
    def wrapper(self, *args, **kwds):
        """Wrapper function"""
        count = self._redis.incr(method.__qualname__)
        return method(self, *args, **kwds)
    return wrapper


class Cache:
    """Class cache"""
    def __init__(self):
        """Init method"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Stores a data in reddis"""
        r_id = str(uuid.uuid4())
        self._redis.set(r_id, data)
        return (r_id)

    @count_calls
    def get(
            self,
            key: str,
            fn: Callable = None,
            ) -> Union[str, bytes, int, float]:
        """Retrieves from a database"""
        data = self._redis.get(key)
        if fn is not None:
            return fn(data)
        return data

    @count_calls
    def get_str(self, key: str) -> str:
        """Convert to string"""
        return self.get(key, lambda x: x.decode('utf-8'))

    @count_calls
    def get_int(self, key: str) -> int:
        """Convert to int"""
        return self.get(key, lambda x: int(x))
