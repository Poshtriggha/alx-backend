#!/usr/bin/env python3
"""Defines a MRUCache class that inherits from BaseCaching"""

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """A caching system using MRU algorithm"""

    def __init__(self):
        """Initialize the MRUCache instance"""
        super().__init__()

    def put(self, key, item):
        """Assigns item to key in self.cache_data"""
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # If cache is full, discard the most recently used item
                mru_key = next(reversed(self.cache_data))
                del self.cache_data[mru_key]
                print("DISCARD:", mru_key)
            self.cache_data[key] = item

    def get(self, key):
        """Returns the value linked to key in self.cache_data"""
        if key is not None:
            if key in self.cache_data:
                # If key exists, move it to the end of the cache data
                value = self.cache_data.pop(key)
                self.cache_data[key] = value
                return value
        return None
