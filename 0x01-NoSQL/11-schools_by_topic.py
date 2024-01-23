#!/usr/bin/env python3
"""Comment"""


def schools_by_topic(mongo_collection, topic):
    """Comment"""
    query = {"topics": topic}
    result_filtered = mongo_collection.find(query)
    result = []
    for item in result_filtered:
        result.append(item)
    return (result)
