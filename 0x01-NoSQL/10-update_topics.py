#!/usr/bin/env python3
"""Comment"""


def update_topics(mongo_collection, name, topics):
    """Comment"""
    update_data = {"$set": {'topics': topics}}
    filter_data = {'name': name}
    result = mongo_collection.update_many(filter_data, update_data)
