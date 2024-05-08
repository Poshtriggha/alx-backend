#!/usr/bin/env python3
"""Defines a BasicCache class that inherits from BaseCaching"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """A caching system without a limit"""

    def put(self, key, item):
        """Assigns item to key in self.cache_data"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Returns the value linked to key in self.cache_data"""
        if key is not None:
            return self.cache_data.get(key)
        return None
