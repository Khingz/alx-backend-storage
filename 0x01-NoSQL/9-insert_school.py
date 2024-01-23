#!/usr/bin/env python3
"""Insert in python"""


def insert_school(mongo_collection, **kwargs):
    new = mongo_collection.insert_one(kwargs)
    return (new.inserted_id)
