#!/usr/bin/env python3
"""List mongo document"""


def list_all(mongo_collection):
    """List mongo document from collection"""
    result = mongo_collection.find()
    final_result = []
    for item in result:
        final_result.append(item)
    return (final_result)
