#!/usr/bin/env python3
"""Defines a LRUCache class that inherits from BaseCaching"""

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """A caching system using LRU algorithm"""

    def __init__(self):
        """Initialize the LRUCache instance"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Assigns item to key in self.cache_data"""
        if key is not None and item is not None:
            if key in self.cache_data:
                # If key exists, remove it from the order
                self.order.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # If cache is full, discard the least recently used item
                lru_key = self.order.pop(0)
                del self.cache_data[lru_key]
                print("DISCARD:", lru_key)
            self.cache_data[key] = item
            self.order.append(key)

    def get(self, key):
        """Returns the value linked to key in self.cache_data"""
        if key is not None:
            if key in self.cache_data:
                # If key exists, move it to the end of the order
                self.order.remove(key)
                self.order.append(key)
                return self.cache_data[key]
        return None
