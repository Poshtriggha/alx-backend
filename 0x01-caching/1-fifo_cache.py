#!/usr/bin/env python3
"""Defines a FIFOCache class that inherits from BaseCaching"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """A caching system using FIFO algorithm"""

    def __init__(self):
        """Initialize the FIFOCache instance"""
        super().__init__()

    def put(self, key, item):
        """Assigns item to key in self.cache_data"""
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # If cache is full, discard the first item (FIFO)
                discarded_key = next(iter(self.cache_data))
                del self.cache_data[discarded_key]
                print("DISCARD:", discarded_key)
            self.cache_data[key] = item

    def get(self, key):
        """Returns the value linked to key in self.cache_data"""
        if key is not None:
            return self.cache_data.get(key)
        return None
