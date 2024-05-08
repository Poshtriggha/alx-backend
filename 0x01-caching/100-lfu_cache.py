#!/usr/bin/env python3
"""Defines a LFUCache class that inherits from BaseCaching"""

from base_caching import BaseCaching

class LFUCache(BaseCaching):
    """A caching system using LFU algorithm"""

    def __init__(self):
        """Initialize the LFUCache instance"""
        super().__init__()
        self.frequency = {}  # Dictionary to store the frequency of each key
        self.time = {}  # Dictionary to store the access time of each key
        self.current_time = 0  # Initialize current_time

    def put(self, key, item):
        """Assigns item to the dictionary self.cache_data"""
        if key is None or item is None:
            return

        # If key already exists, update its value and frequency
        if key in self.cache_data:
            self.cache_data[key] = item
            self.frequency[key] += 1
        else:
            # If cache is full, discard the least frequently used item
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                min_freq = min(self.frequency.values())
                lfu_keys = [k for k, v in self.frequency.items() if v == min_freq]
                lru_key = min(lfu_keys, key=lambda k: self.time[k])
                del self.cache_data[lru_key]
                del self.frequency[lru_key]
                del self.time[lru_key]
                print(f"DISCARD: {lru_key}")

            # Add new item to cache
            self.cache_data[key] = item
            self.frequency[key] = 1
            self.time[key] = self.current_time

        self.current_time += 1

    def get(self, key):
        """Returns the value in self.cache_data linked to key"""
        if key is None or key not in self.cache_data:
            return None

        # Update the frequency and access time of the accessed key
        self.frequency[key] += 1
        self.time[key] = self.current_time
        self.current_time += 1

        return self.cache_data[key]
