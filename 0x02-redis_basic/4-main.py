#!/usr/bin/env python3
""" Main file """

Cache = __import__('exercise').Cache
replay = __import__('exercise').replay
cache = Cache()

cache.store(b"first")
cache.store(b"second")
cache.store(b"third")
replay(cache.store)
