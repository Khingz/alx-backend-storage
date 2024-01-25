#!/usr/bin/env python3
"""Commnet"""
import redis
import requests
from functools import wraps
from typing import Callable


redis_store = redis.Redis()


def cache(method: Callable) -> Callable:
    """Cache wrapper"""
    @wraps(method)
    def wrapper(url) -> str:
        """wrapper method"""
        redis_store.incr("count:{}".format(url))
        if result:
            return result.decode('utf-8')
        result = method(url)
        redis_store.set("count:{}".format(url))
        redis_store.setex("count:{}".format(url), 10, result)
        return result
    return invoker


def get_page(url: str) -> str:
    """obtain the HTML content of a particular URL"""
    content = requests.get(url).text
    return (content)
