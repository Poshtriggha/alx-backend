#!/usr/bin/env python3
"""AAA"""

from base_caching import BaseCaching

class MRUCache(BaseCaching):
    """AAA"""
    def __init__(self):
        """AAA"""
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """AAA"""
        if key and item:
            if self.cache_data.get(key):
                self.stack.remove(key)
            while len(self.stack) >= self.MAX_ITEMS:
                delete = self.stack.pop()
                self.cache_data.pop(delete)
                print('DISCARD: {}'.format(delete))
            self.stack.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """AAA"""
        if self.cache_data.get(key):
            self.stack.remove(key)
            self.stack.append(key)
        return self.cache_data.get(key)
