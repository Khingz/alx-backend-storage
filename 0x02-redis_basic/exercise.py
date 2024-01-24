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


def call_history(method: Callable) -> Callable:
    """Call history decorator function"""
    @wraps(method)
    def wrapper(self, *args, **kwds):
        """Wrapper function"""
        self._redis.rpush(
                "{}:inputs".format(method.__qualname__),
                str(args)
                )
        output = method(self, *args, **kwds)
        self._redis.rpush(
                "{}:outputs".format(method.__qualname__),
                str(output)
                )
        return (output)
    return wrapper


def replay(method: Callable) -> Callable:
    """Replays a method"""
    @wraps(method)
    def wrapper(self, *args, **kwds):
        """Wrapper function"""
        key = method.__qualname__
        result = method(self, *args, **kwds)
        input_key = "{}:input".format(key)
        input_his = redis_client.lrange(input_key, 0, -1)
        output_key = "{}:output".format(key)
        output_his = redis_client.lrange(output_key, 0, -1)
        for i, o in zip(input_his, output_his):
            print("{}({}) -> {}".format(key, i, o))
        return (result)
    return wrapper


class Cache:
    """Class cache"""
    def __init__(self):
        """Init method"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Stores a data in reddis"""
        r_id = str(uuid.uuid4())
        self._redis.set(r_id, data)
        return (r_id)

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

    def get_str(self, key: str) -> str:
        """Convert to string"""
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> int:
        """Convert to int"""
        return self.get(key, lambda x: int(x))
