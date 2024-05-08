#!/usr/bin/env python3
"""Defines a LIFOCache class that inherits from BaseCaching"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """A caching system using LIFO algorithm"""

    def __init__(self):
        """Initialize the LIFOCache instance"""
        super().__init__()

    def put(self, key, item):
        """Assigns item to key in self.cache_data"""
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # If cache is full, discard the last item (LIFO)
                last_key = list(self.cache_data.keys())[-1]
                del self.cache_data[last_key]
                print("DISCARD:", last_key)
            self.cache_data[key] = item

    def get(self, key):
        """Returns the value linked to key in self.cache_data"""
        if key is not None:
            return self.cache_data.get(key)
        return None
