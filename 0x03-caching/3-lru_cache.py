#!/usr/bin/python3
"""LRU Caching
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """Class LRUCache"""
    def __init__(self):
        """Constructor"""
        super().__init__()
        self.line = []

    def put(self, key, item):
        """ Add an item in the cache with LRU algorithm """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.line.remove(key)
            self.line.append(key)
            self.cache_data[key] = item

            if len(self.cache_data) > self.MAX_ITEMS:
                erase = self.line.pop(0)
                self.cache_data.pop(erase)
                print('DISCARD: {}'.format(erase))

    def get(self, key):
        """ Get an item by key """
        if key is not None and key in self.cache_data:
            self.line.remove(key)
            self.line.append(key)
        return self.cache_data.get(key)
