#!/usr/bin/env python3
"""Defines a LFUCache class that inherits from BaseCaching"""

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """A caching system using LFU algorithm"""

    def __init__(self):
        """Initialize the LFUCache instance"""
        super().__init__()
        self.frequency = {}

    def put(self, key, item):
        """Assigns item to key in self.cache_data"""
        if key is not None and item is not None:
            if key in self.cache_data:
                # If key exists, increment its frequency
                self.frequency[key] += 1
            else:
                # If key doesn't exist, initialize its frequency
                self.frequency[key] = 1

            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # If cache is full, find the least frequency used item
                min_freq = min(self.frequency.values())
                least_freq_used_keys = [k for k, v in self.frequency.items() if v == min_freq]
                # If there's more than one least frequency used item, use LRU to break the tie
                if len(least_freq_used_keys) > 1:
                    lru_key = min(self.cache_data, key=lambda k: self.cache_data[k]['time'])
                    del self.cache_data[lru_key]
                    del self.frequency[lru_key]
                    print("DISCARD:", lru_key)
                else:
                    lfu_key = least_freq_used_keys[0]
                    del self.cache_data[lfu_key]
                    del self.frequency[lfu_key]
                    print("DISCARD:", lfu_key)

            self.cache_data[key] = {'value': item, 'time': self.time}
            self.time += 1

    def get(self, key):
        """Returns the value linked to key in self.cache_data"""
        if key is not None and key in self.cache_data:
            # Increment the frequency of the accessed key
            self.frequency[key] += 1
            # Update the access time of the accessed key
            self.cache_data[key]['time'] = self.time
            self.time += 1
            return self.cache_data[key]['value']
        return None
