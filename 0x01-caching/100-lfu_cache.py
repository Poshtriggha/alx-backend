#!/usr/bin/python3
""" 5. LFU caching
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    def __init__(self):
        """ Initializes the LFUCache instance
        """
        super().__init__()
        self.frequency = {}  # Stores the frequency of each key
        self.age = {}  # Stores the age of each key
        self.counter = 0  # Tracks the current age

    def put(self, key, item):
        """ Adds an item to the cache
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Update existing key
            self.cache_data[key] = item
            self.frequency[key] += 1
            self.age[key] = self.counter
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Find least frequently used keys
            lfu_keys = [k for k, v in self.frequency.items() if v == min(
                self.frequency.values())]
            # Find least recently used key among the least frequently used keys
            lru_key = min(lfu_keys, key=lambda k: self.age[k])
            # Remove least recently used key
            del self.cache_data[lru_key]
            del self.frequency[lru_key]
            del self.age[lru_key]
            print(f"DISCARD: {lru_key}")

        self.cache_data[key] = item
        self.frequency[key] = 1
        self.age[key] = self.counter

    def get(self, key):
        """ Retrieves an item by key
        """
        if key is None or key not in self.cache_data:
            return None

        # Update frequency and age for the accessed key
        self.frequency[key] += 1
        self.age[key] = self.counter
        return self.cache_data[key]
