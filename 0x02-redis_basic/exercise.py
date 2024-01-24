#!/usr/bin/env python3
"""Comment"""
import uuid
import redis
from typing import Union


class Cache:
    """Class cache"""
    def __init__(self):
        """Init method"""
        self._redis = redis.Redis()
        self._redis.flushdb()


    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Stores a data in reddis"""
        r_id = str(uuid.uuid4())
        self._redis.set(r_id, data)
        return (r_id)


    def get(
            key: str,
            fn: Callable = None,
            ) -> Union[str, bytes, int, float]:
        """Retrieves from a database"""
        data = self._redis.get(key)
        if fn is not None:
            return fn(data)
        return data


    def get_str(self, key: str) -> str:
        """Convert to string"""
        return self.get(key, fn=str)


    def get_int(self, key: str) -> int:
        """Convert to int"""
        return self.get(key, fn=int)

