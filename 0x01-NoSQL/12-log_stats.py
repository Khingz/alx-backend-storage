#!/usr/bin/env python3
"""Commant"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx
    print("{} logs".format(collection.count_documents({})))
    print("Methods:")
    method = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for med in method:
        query = {"method": med}
        count = collection.count_documents(query)
        print("\tmethod {}: {}".format(med, count))
    query = {"method": "GET", "path": "/status"}
    status = collection.count_documents(query)
    print("{} status check".format(status))
